# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger_test.py
options = debugger.QuantizationDebugOptions(
    layer_debug_metrics={'l1_norm': lambda diffs: np.mean(np.abs(diffs))},
    fully_quantize=quantized_io,
    denylisted_nodes=['Identity'])
# TODO(b/195084873): Count the number of NumericVerify op.
with self.assertRaisesRegex(
    ValueError, 'Please check if the quantized model is in debug mode'):
    _ = debugger.QuantizationDebugger(
        converter=_quantize_converter(self.tf_model_root, self.tf_model,
                                      _calibration_gen),
        debug_dataset=_calibration_gen,
        debug_options=options)
