# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Run the calibration and return the calibrated GraphDef.

    Args:
      fetch_names: a list of output tensor name to fetch during calibration.
      num_runs: number of runs of the graph during calibration.
      feed_dict_fn: a function that returns a dictionary mapping input names (as
        strings) in the GraphDef to be calibrated to values (e.g. Python list,
        numpy arrays, etc). One and only one of `feed_dict_fn` and
        `input_map_fn` should be specified.
      input_map_fn: a function that returns a dictionary mapping input names (as
        strings) in the GraphDef to be calibrated to Tensor objects. The values
        of the named input tensors in the GraphDef to be calibrated will be
        re-mapped to the respective `Tensor` values during calibration. One and
        only one of `feed_dict_fn` and `input_map_fn` should be specified.

    Raises:
      ValueError: if the input combination is invalid.
      RuntimeError: if this method is called in eager mode.

    Returns:
      The GraphDef after the calibration.
    """
assert self._converted
assert self._need_calibration
assert not self._calibration_data_collected

if (feed_dict_fn and input_map_fn) or (not feed_dict_fn and
                                       not input_map_fn):
    raise ValueError(
        "Should specify one and only one of feed_dict_fn and input_map_fn.")

if input_map_fn:
    for k, v in input_map_fn().items():
        if not isinstance(k, str):
            raise ValueError("Keys of input_map_fn must be of type str")
        if not isinstance(v, ops.Tensor):
            raise ValueError("Values of input_map_fn must be of type tf.Tensor")

self._calibration_graph = ops.Graph()
with self._calibration_graph.as_default():
    fetches = importer.import_graph_def(
        self._converted_graph_def,
        input_map=input_map_fn() if input_map_fn else None,
        return_elements=fetch_names,
        name="")

calibrate_rewriter_cfg = rewriter_config_pb2.RewriterConfig()
if self._test_only_disable_non_trt_optimizers:
    trt_utils.disable_non_trt_optimizers_in_rewriter_config(
        calibrate_rewriter_cfg)

# Set allow_soft_placement=True to run the graph for calibration so that
# OPs supported by TensorRT but don't have a GPU implementation are allowed
# to execute on CPU.
calibrate_config = config_pb2.ConfigProto(
    allow_soft_placement=True,
    graph_options=config_pb2.GraphOptions(
        rewrite_options=calibrate_rewriter_cfg))

with session.Session(
    graph=self._calibration_graph,
    config=calibrate_config) as calibration_sess:
    for _ in range(num_runs):
        calibration_sess.run(
            fetches, feed_dict=feed_dict_fn() if feed_dict_fn else None)

    # Maps device name to the corresponding get_calibration_data.
    #
    # TODO(laigd): a better way would be to use calibration_sess to list
    # all the devices, add one get_calibration_data for each device, and
    # fetch each such op for every resource until its found. This can work
    # even when the device of the TRTEngineOp is empty or not fully specified.
    device_to_get_resource_op_map = {}

    with self._calibration_graph.as_default():
        resource_name_input = array_ops.placeholder(dtypes.string)

        for node in self._converted_graph_def.node:
            if node.op == _TRT_ENGINE_OP_NAME:
                # Adds the get_calibration_data op for the device if not done
                # before. We only add one such op for each device.
                # TODO(laigd): What if the device is empty?????
                if node.device not in device_to_get_resource_op_map:
                    with self._calibration_graph.device(node.device):
                        serialized_resources_output = (
                            gen_trt_ops.get_calibration_data_op(resource_name_input))
                    device_to_get_resource_op_map[node.device] = (
                        serialized_resources_output)

                # Get the calibration resource.
                calibration_result = calibration_sess.run(
                    device_to_get_resource_op_map[node.device],
                    feed_dict={
                        resource_name_input: _get_canonical_engine_name(node.name)
                    })
                node.attr["calibration_data"].s = calibration_result

    self._calibration_data_collected = True

exit(self._converted_graph_def)
