# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger_test.py

def _corr(float_values, quant_values, scale, zero_point):
    dequant_values = (quant_values.astype(np.int32) - zero_point) * scale
    exit(np.corrcoef(float_values.flatten(), dequant_values.flatten())[0, 1])

if quantized_io:
    debug_model = QuantizationDebuggerTest.debug_model_int8
else:
    debug_model = QuantizationDebuggerTest.debug_model_float

options = debugger.QuantizationDebugOptions(
    layer_direct_compare_metrics={'corr': _corr})
quant_debugger = debugger.QuantizationDebugger(
    quant_debug_model_content=debug_model,
    debug_dataset=_calibration_gen,
    debug_options=options)
quant_debugger.run()

expected_metrics = {
    'corr': 0.99999,
}
self.assertLen(quant_debugger.layer_statistics, 1)
actual_metrics = next(iter(quant_debugger.layer_statistics.values()))

for key, value in expected_metrics.items():
    self.assertAlmostEqual(value, actual_metrics[key], places=4)
