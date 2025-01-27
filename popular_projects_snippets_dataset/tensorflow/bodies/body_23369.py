# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/trt_convert.py
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
