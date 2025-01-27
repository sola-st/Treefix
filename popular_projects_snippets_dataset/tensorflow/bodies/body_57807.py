# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
func, calibration_gen = self._getSqrtModel()
converter = lite.TFLiteConverterV2.from_concrete_functions(
    [func.get_concrete_function()])
converter.representative_dataset = calibration_gen
converter.optimizations = [lite.Optimize.DEFAULT]
converter.experimental_new_quantizer = mlir_quantizer
quantized_model = converter.convert()

# Because assertions on the model later, we opt out applying default TFLite
# delegates (i.e. the XNNPACK delegate).
interpreter = Interpreter(
    model_content=quantized_model,
    experimental_op_resolver_type=OpResolverType
    .BUILTIN_WITHOUT_DEFAULT_DELEGATES)
interpreter.allocate_tensors()
# The model should have only one sqrt op.
op_details = interpreter._get_ops_details()
self.assertLen(op_details, 1)
self.assertEqual(op_details[0]['op_name'], 'SQRT')
