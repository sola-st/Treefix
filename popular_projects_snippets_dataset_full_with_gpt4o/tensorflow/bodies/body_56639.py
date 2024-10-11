# Extracted from ./data/repos/tensorflow/tensorflow/lite/tools/optimize/debugging/python/debugger_test.py
options = debugger.QuantizationDebugOptions(
    layer_debug_metrics={'l1_norm': lambda diffs: np.mean(np.abs(diffs))},
    fully_quantize=quantized_io)
quant_debugger = debugger.QuantizationDebugger(
    converter=_quantize_converter(self.tf_model_root, self.tf_model,
                                  _calibration_gen),
    debug_dataset=_calibration_gen,
    debug_options=options)

options.denylisted_ops = ['CONV_2D']
# TODO(b/195084873): The exception is expected to check whether selective
# quantization was done properly, since after the selective quantization
# the model will have no quantized layers thus have no NumericVerify ops,
# resulted in this exception. Marked with a bug to fix this in more
# straightforward way.
with self.assertRaisesRegex(
    ValueError, 'Please check if the quantized model is in debug mode'):
    quant_debugger.options = options
