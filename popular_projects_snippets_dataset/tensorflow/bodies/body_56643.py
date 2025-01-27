# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger_test.py
debug_model = QuantizationDebuggerTest.debug_model_float
debugger.QuantizationDebugger(
    quant_debug_model_content=debug_model, debug_dataset=_calibration_gen)
increase_call.assert_called_once()
