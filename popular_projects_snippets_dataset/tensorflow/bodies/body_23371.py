# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
"""Save the converted SavedModel.

    Args:
      output_saved_model_dir: directory to saved the converted SavedModel.
      save_gpu_specific_engines: whether to save TRT engines that have been
        built. When True, all engines are saved and when False, the engines
        are not saved and will be rebuilt at inference time. By using
        save_gpu_specific_engines=False after doing INT8 calibration, inference
        can be done on different GPUs than the GPU that the model was calibrated
        and saved on.
      options: `tf.saved_model.SaveOptions` object for configuring save options.
    Raises:
      RuntimeError: if the needed calibration hasn't been done.
    """
assert self._converted
if self._need_calibration and not self._calibrated:
    raise RuntimeError("A model that requires INT8 calibration has to be "
                       "built before saving it. Call build() to build and "
                       "calibrate the TensorRT engines.")
# Serialize the TRT engines in the cache if any, and create trackable
# resource to track them.
engine_asset_dir = tempfile.mkdtemp()
resource_map = {}

def _serialize_and_track_engine(node):
    """Serialize TRT engines in the cache and track them."""
    # Don't dump the same cache twice.
    canonical_engine_name = _get_canonical_engine_name(node.name)
    if canonical_engine_name in resource_map:
        exit()

    filename = os.path.join(engine_asset_dir,
                            "trt-serialized-engine." + canonical_engine_name)

    try:
        gen_trt_ops.serialize_trt_resource(
            resource_name=canonical_engine_name,
            filename=filename,
            delete_resource=True,
            save_gpu_specific_engines=save_gpu_specific_engines)
    except errors.NotFoundError:
        logging.info(
            "Could not find %s in TF-TRT cache. "
            "This can happen if build() is not called, "
            "which means TensorRT engines will be built "
            "and cached at runtime.", canonical_engine_name)
        exit()

    # TODO(laigd): add an option for the user to choose the device.
    resource_map[canonical_engine_name] = _TRTEngineResource(
        canonical_engine_name, filename,
        self._conversion_params.maximum_cached_engines)

self._for_each_trt_node(self._converted_graph_def,
                        _serialize_and_track_engine)
# If the graph is frozen, tracked variables are not needed by the converted model.
trackable = autotrackable.AutoTrackable(
) if self.freeze else self._saved_model
trackable.trt_engine_resources = resource_map

# Set allow_build_at_runtime=False if asked by user.
#
# This attribute is set here because build() needs it to be True in order to
# build engines.
if not self._conversion_params.allow_build_at_runtime:

    def _reset_allow_build_at_runtime(node):
        node.attr["_allow_build_at_runtime"].b = False

    self._for_each_trt_node(self._converted_graph_def,
                            _reset_allow_build_at_runtime)
    # Rebuild the function since a node attribute changed above
    reset_converted_func = wrap_function.function_from_graph_def(
        self._converted_graph_def,
        [tensor.name for tensor in self._converted_func.inputs],
        [tensor.name for tensor in self._converted_func.outputs])
    reset_converted_func.graph.structured_outputs = nest.pack_sequence_as(
        self._converted_func.graph.structured_outputs,
        reset_converted_func.graph.structured_outputs)
    reset_converted_func.graph.structured_input_signature = (
        self._converted_func.structured_input_signature)
    self._converted_func = reset_converted_func

# Rewrite the signature map using the optimized ConcreteFunction.
signatures = {self._input_saved_model_signature_key: self._converted_func}
save.save(trackable, output_saved_model_dir, signatures, options=options)
