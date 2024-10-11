# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
saved_model_dir = self._createV2QATSavedModelWithFloatOpsAtEnd()
converter = lite.TFLiteConverterV2.from_saved_model(saved_model_dir)
converter.optimizations = [lite.Optimize.DEFAULT]
quantized_model = converter.convert()

# Because assertions on the model later, we opt out applying default TFLite
# delegates (i.e. the XNNPACK delegate).
interpreter = Interpreter(
    model_content=quantized_model,
    experimental_op_resolver_type=OpResolverType
    .BUILTIN_WITHOUT_DEFAULT_DELEGATES)
interpreter.allocate_tensors()
# The model should have LOGISTIC op, instead of DEQUANTIZE op.
op_details = interpreter._get_ops_details()
self.assertEqual(op_details[len(op_details) - 1]['op_name'], 'LOGISTIC')
