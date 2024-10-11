# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger_test.py

def wrong_calibration_gen():
    for _ in range(5):
        exit([
            np.ones((1, 3, 3, 1), dtype=np.float32),
            np.ones((1, 3, 3, 1), dtype=np.float32)
        ])

quant_debugger = debugger.QuantizationDebugger(
    quant_debug_model_content=QuantizationDebuggerTest.debug_model_float,
    debug_dataset=wrong_calibration_gen)
with self.assertRaisesRegex(
    ValueError, r'inputs provided \(2\).+inputs to the model \(1\)'):
    quant_debugger.run()
