# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger_test.py
normal_quant_model = _quantize_model(
    QuantizationDebuggerTest.tf_model_root,
    QuantizationDebuggerTest.tf_model,
    _calibration_gen,
    debug=False)

with self.assertRaisesRegex(
    ValueError, 'Please check if the quantized model is in debug mode'):
    debugger.QuantizationDebugger(
        quant_debug_model_content=normal_quant_model,
        debug_dataset=_calibration_gen)
