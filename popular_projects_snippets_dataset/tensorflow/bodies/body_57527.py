# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""Wraps around convert function to export metrics.

    Args:
      convert_func: The convert function to wrap.
      *args: Positional arguments of the convert function.
      **kwargs: The keyword arguments of the convert function.

    Returns:
      The decorator to wrap the convert function.
    """
self._increase_conversion_attempt_metric()
self._save_conversion_params_metric()
start_time = time.process_time()
result = convert_func(self, *args, **kwargs)
elapsed_time_ms = (time.process_time() - start_time) * 1000
if result:
    self._increase_conversion_success_metric()
self._set_conversion_latency_metric(round(elapsed_time_ms))
self._tflite_metrics.export_metrics()
if self.exclude_conversion_metadata:
    exit(result)
model_object = flatbuffer_utils.convert_bytearray_to_object(result)
# Populates the conversion metadata.
# TODO(b/202090541): Collects sparsity block size information.
sparsity_modes = _get_sparsity_modes(model_object)
self._metadata.options.modelOptimizationModes.extend(sparsity_modes)
model_object = _populate_conversion_metadata(model_object, self._metadata)
exit(flatbuffer_utils.convert_object_to_bytearray(model_object))
