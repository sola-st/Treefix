# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Initializes the converter.

    Args:
      input_saved_model_dir: the directory to load the SavedModel which contains
        the input graph to transforms. Used only when input_graph_def is None.
      input_saved_model_tags: list of tags to load the SavedModel.
      input_saved_model_signature_key: the key of the signature to optimize the
        graph for.
      input_graph_def: a GraphDef object containing a model to be transformed.
        If set to None, the graph will be read from the SavedModel loaded from
        input_saved_model_dir.
      nodes_denylist: list of node names to prevent the converter from touching.
      max_batch_size: max size for the input batch.
      max_workspace_size_bytes: the maximum GPU temporary memory which the TRT
        engine can use at execution time. This corresponds to the
        'workspaceSize' parameter of nvinfer1::IBuilder::setMaxWorkspaceSize().
      precision_mode: one of TrtPrecisionMode.supported_precision_modes().
      minimum_segment_size: the minimum number of nodes required for a subgraph
        to be replaced by TRTEngineOp.
      is_dynamic_op: whether to generate dynamic TRT ops which will build the
        TRT network and engine at run time.
      maximum_cached_engines: max number of cached TRT engines in dynamic TRT
        ops. If the number of cached engines is already at max but none of them
        can serve the input, the TRTEngineOp will fall back to run the TF
        function based on which the TRTEngineOp is created.
      use_calibration: this argument is ignored if precision_mode is not INT8.
        If set to True, a calibration graph will be created to calibrate the
        missing ranges. The calibration graph must be converted to an inference
        graph by running calibration with calibrate(). If set to False,
        quantization nodes will be expected for every tensor in the graph
        (excluding those which will be fused). If a range is missing, an error
        will occur. Please note that accuracy may be negatively affected if
        there is a mismatch between which tensors TRT quantizes and which
        tensors were trained with fake quantization.

    Raises:
      ValueError: if the combination of the parameters is invalid.
      RuntimeError: if this class is used in TF 2.0.
    """
if context.executing_eagerly():
    raise RuntimeError(
        "Please use tf.experimental.tensorrt.Converter in TF 2.0.")

if input_graph_def and input_saved_model_dir:
    raise ValueError(
        "Can only specify one of input_graph_def and input_saved_model_dir")
if not input_graph_def and not input_saved_model_dir:
    raise ValueError("Must specify one of input_graph_def and "
                     "input_saved_model_dir")
_check_trt_version_compatibility()

self._input_graph_def = input_graph_def
self._nodes_denylist = nodes_denylist

self._input_saved_model_dir = input_saved_model_dir
self._converted = False
self._grappler_meta_graph_def = None

self._input_saved_model_tags = (
    input_saved_model_tags or [tag_constants.SERVING])
self._input_saved_model_signature_key = (
    input_saved_model_signature_key or
    signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY)

# For calibration usage.
self._calibration_graph = None
self._calibration_data_collected = False
self._need_calibration = (
    ((precision_mode == TrtPrecisionMode.INT8) or
     (precision_mode == TrtPrecisionMode.INT8.lower())) and use_calibration)
if self._need_calibration and not is_dynamic_op:
    logging.warn(
        "INT8 precision mode with calibration is supported with "
        "dynamic TRT ops only. Disregarding is_dynamic_op parameter.")
    is_dynamic_op = True

self._is_dynamic_op = is_dynamic_op
if is_dynamic_op:
    self._max_batch_size = None
    if max_batch_size is not None:
        logging.warn("When is_dynamic_op==True max_batch_size should be None")
else:
    if not isinstance(max_batch_size, int):
        raise ValueError("When is_dynamic_op==False max_batch_size should be "
                         "an integer")
    self._max_batch_size = max_batch_size

self._conversion_params = TrtConversionParams(
    max_workspace_size_bytes=max_workspace_size_bytes,
    precision_mode=precision_mode,
    minimum_segment_size=minimum_segment_size,
    maximum_cached_engines=maximum_cached_engines,
    use_calibration=use_calibration,
    allow_build_at_runtime=True)
_check_conversion_params(self._conversion_params)

self._test_only_disable_non_trt_optimizers = False
