# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Initialize the converter.

    Args:
      input_saved_model_dir: the directory to load the SavedModel which contains
        the input graph to transforms. Required.
      input_saved_model_tags: list of tags to load the SavedModel.
      input_saved_model_signature_key: the key of the signature to optimize the
        graph for.
      use_dynamic_shape: whether to enable dynamic shape support. None is
        equivalent to False in the current implementation.
      dynamic_shape_profile_strategy: one of the strings in
        supported_profile_strategies(). None is equivalent to Range in the
        current implementation.
      max_workspace_size_bytes: the maximum GPU temporary memory that the TRT
        engine can use at execution time. This corresponds to the
        'workspaceSize' parameter of nvinfer1::IBuilder::setMaxWorkspaceSize().
      precision_mode: one of the strings in
        TrtPrecisionMode.supported_precision_modes().
      minimum_segment_size: the minimum number of nodes required for a subgraph
        to be replaced by TRTEngineOp.
      maximum_cached_engines: max number of cached TRT engines for dynamic TRT
        ops. Created TRT engines for a dynamic dimension are cached. If the
        number of cached engines is already at max but none of them supports the
        input shapes, the TRTEngineOp will fall back to run the original TF
        subgraph that corresponds to the TRTEngineOp.
      use_calibration: this argument is ignored if precision_mode is not INT8.
        If set to True, a calibration graph will be created to calibrate the
        missing ranges. The calibration graph must be converted to an inference
        graph by running calibration with calibrate(). If set to False,
        quantization nodes will be expected for every tensor in the graph
        (excluding those which will be fused). If a range is missing, an error
        will occur. Please note that accuracy may be negatively affected if
        there is a mismatch between which tensors TRT quantizes and which
        tensors were trained with fake quantization.
      allow_build_at_runtime: whether to allow building TensorRT engines during
        runtime if no prebuilt TensorRT engine can be found that can handle the
        given inputs during runtime, then a new TensorRT engine is built at
        runtime if allow_build_at_runtime=True, and otherwise native TF is used.
      conversion_params: a TrtConversionParams instance (deprecated).

    Raises:
      ValueError: if the combination of the parameters is invalid.
    """
assert context.executing_eagerly()
if conversion_params is None:
    conversion_params = TrtConversionParams(
        max_workspace_size_bytes=max_workspace_size_bytes,
        precision_mode=precision_mode,
        minimum_segment_size=minimum_segment_size,
        maximum_cached_engines=maximum_cached_engines,
        use_calibration=use_calibration,
        allow_build_at_runtime=allow_build_at_runtime)

_check_trt_version_compatibility()
_check_conversion_params(conversion_params, is_v2=True)

self._conversion_params = conversion_params
self._input_saved_model_dir = input_saved_model_dir
self._input_saved_model_tags = (
    input_saved_model_tags or [tag_constants.SERVING])
self._input_saved_model_signature_key = (
    input_saved_model_signature_key or
    signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY)
self.freeze = not trt_utils.is_experimental_feature_activated(
    "disable_graph_freezing")

self._need_calibration = ((
    (conversion_params.precision_mode == TrtPrecisionMode.INT8) or
    (conversion_params.precision_mode == TrtPrecisionMode.INT8.lower())) and
                          conversion_params.use_calibration)

self._calibration_input_fn = None

self._converted = False
self._device = None
self._build_called_once = False
self._calibrated = False

if use_dynamic_shape is None:
    self._use_dynamic_shape = False
else:
    self._use_dynamic_shape = use_dynamic_shape

if not self.freeze and not self._use_dynamic_shape:
    logging.warn(
        "Disabling graph freezing is only possible in dynamic shape mode."
        " The graph will be frozen.")
    self.freeze = True

self._profile_strategy = "Unknown"
if self._use_dynamic_shape:
    if dynamic_shape_profile_strategy is None:
        self._profile_strategy = PROFILE_STRATEGY_RANGE
    else:
        self._verify_profile_strategy(dynamic_shape_profile_strategy)
        self._profile_strategy = dynamic_shape_profile_strategy

    # Fields to support TF-TRT testing and shouldn't be used for other purpose.
self._test_only_disable_non_trt_optimizers = False
