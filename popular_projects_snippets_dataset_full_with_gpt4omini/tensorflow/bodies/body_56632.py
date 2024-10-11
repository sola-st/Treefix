# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger_test.py
if quantized_io:
    debug_model = QuantizationDebuggerTest.debug_model_int8
else:
    debug_model = QuantizationDebuggerTest.debug_model_float
options = debugger.QuantizationDebugOptions(
    model_debug_metrics={'stdev': lambda x, y: np.std(x[0] - y[0])})
quant_debugger = debugger.QuantizationDebugger(
    quant_debug_model_content=debug_model,
    float_model_content=QuantizationDebuggerTest.float_model,
    debug_dataset=_calibration_gen,
    debug_options=options)
quant_debugger.run()

expected_metrics = {'stdev': 0.050998904}
actual_metrics = quant_debugger.model_statistics

self.assertCountEqual(expected_metrics.keys(), actual_metrics.keys())
for key, value in expected_metrics.items():
    self.assertAlmostEqual(value, actual_metrics[key], places=5)
