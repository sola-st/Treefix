# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
self._optimizations = optimizations
for deprecated_optimization in [
    Optimize.OPTIMIZE_FOR_SIZE, Optimize.OPTIMIZE_FOR_LATENCY
]:
    if deprecated_optimization in self._optimizations:
        logging.warning(
            "Optimization option %s is deprecated, please use optimizations="
            "[Optimize.DEFAULT] instead.", deprecated_optimization)

self._target_spec = target_spec
self._representative_dataset = representative_dataset
self._graph_def = graph_def

self._validate_int8_required()
self._disable_per_channel = disable_per_channel

self._enable_new_dynamic_range_quantizer = (
    experimental_new_dynamic_range_quantizer)
# Allow training with lower than 8 bit weights to be converted
# to constants with trained scale.
self._experimental_low_bit_qat = experimental_low_bit_qat

self._full_integer_quantization_bias_type = full_integer_quantization_bias_type
self._validate_full_integer_quantization_bias_type()

self.enable_mlir_variable_quantization = (
    experimental_mlir_variable_quantization)
