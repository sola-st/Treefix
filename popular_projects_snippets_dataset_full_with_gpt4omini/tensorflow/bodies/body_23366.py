# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Convert the input SavedModel in 2.0 format.

    Args:
      calibration_input_fn: a generator function that yields input data as a
        list or tuple or dict, which will be used to execute the converted
        signature for calibration. All the returned input data should have the
        same shape. Example: `def input_fn(): yield input1, input2, input3`

        If dynamic_shape_mode==False, (or if the graph has static input shapes)
        then we run calibration and build the calibrated engine during
        conversion.

        If dynamic_shape_mode==True (and the graph has any unknown input
        shape), then the reference to calibration_input_fn is stored, and the
        calibration is actually performed when we build the engine (see
        build()).

    Raises:
      ValueError: if the input combination is invalid.

    Returns:
      The TF-TRT converted Function.
    """
assert not self._converted

# Creating an empty tensor to fetch queried device
device_requested = array_ops.zeros([]).device

if "gpu" not in device_requested.lower():
    raise ValueError(f"Specified device is not a GPU: {device_requested}")

if "gpu:0" not in device_requested.lower():
    self._device = device_requested
    logging.info(f"Placing imported graph from "
                 f"`{self._input_saved_model_dir}` on device: {self._device}")

if (self._need_calibration and not calibration_input_fn):
    raise ValueError("Should specify calibration_input_fn because INT8 "
                     "calibration is needed")
if (not self._need_calibration and calibration_input_fn):
    raise ValueError("Should not specify calibration_input_fn because INT8 "
                     "calibration is not needed")

self._saved_model = load.load(self._input_saved_model_dir,
                              self._input_saved_model_tags)
func = self._saved_model.signatures[self._input_saved_model_signature_key]
if self.freeze:
    frozen_func = convert_to_constants.convert_variables_to_constants_v2(func)
else:
    inlined_graph_def = _apply_inlining(func)
    _annotate_variable_ops(func, inlined_graph_def)
    frozen_func = _construct_function_from_graph_def(func, inlined_graph_def)
frozen_graph_def = frozen_func.graph.as_graph_def()

# Clear any prior device assignments
logging.info("Clearing prior device assignments in loaded saved model")
for node in frozen_graph_def.node:
    node.device = ""

if self._device is None:
    grappler_meta_graph_def = saver.export_meta_graph(
        graph_def=frozen_graph_def, graph=frozen_func.graph)
else:
    with ops.Graph().as_default() as graph, ops.device(self._device):
        importer.import_graph_def(frozen_graph_def, name="")
        grappler_meta_graph_def = saver.export_meta_graph(
            graph_def=graph.as_graph_def(), graph=graph)

    # Add a collection 'train_op' so that Grappler knows the outputs.
fetch_collection = meta_graph_pb2.CollectionDef()
for array in frozen_func.inputs + frozen_func.outputs:
    fetch_collection.node_list.value.append(array.name)
grappler_meta_graph_def.collection_def["train_op"].CopyFrom(
    fetch_collection)

# Run TRT optimizer in Grappler to convert the graph.
self._converted_graph_def = self._run_conversion(grappler_meta_graph_def)
self._converted_func = _construct_function_from_graph_def(
    func, self._converted_graph_def, frozen_func)

if self._need_calibration:
    # Execute calibration here only if not in dynamic shape mode.
    if not self._need_trt_profiles():
        self._execute_calibration(calibration_input_fn)
    else:
        self._calibration_input_fn = calibration_input_fn

self._converted = True

graphviz_path = os.environ.get("TF_TRT_EXPORT_GRAPH_VIZ_PATH", default=None)
if graphviz_path is not None:
    try:
        trt_utils.draw_graphdef_as_graphviz(
            graphdef=self._converted_func.graph.as_graph_def(add_shapes=True),
            dot_output_filename=graphviz_path)
    except Exception as e:
        logging.error("An Exception occured during the export of the graph "
                      f"visualization: {e}")

exit(self._converted_func)
