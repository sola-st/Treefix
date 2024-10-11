# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite_v2_test.py
"""Convert multiple functions with the shared weight."""
root = self._getMultiFunctionModelWithSharedWeight()
input_data = tf.constant(1., shape=[1])
add_func = root.add.get_concrete_function(input_data)
sub_func = root.sub.get_concrete_function(input_data)
mul_func = root.mul.get_concrete_function(input_data)

save_dir = os.path.join(self.get_temp_dir(), 'saved_model')
save(root, save_dir, {'add': add_func, 'sub': sub_func, 'mul': mul_func})

# Try converting multiple functions.
converter = lite.TFLiteConverterV2.from_saved_model(save_dir)
tflite_model = converter.convert()
self.assertIsNotNone(tflite_model)

# Make sure that the weight tensors are shared.
self.assertLess(len(tflite_model), 1100000)

# TODO(b/184696047): Write down the test codes for multiple signature
#                    runners once the Python API is ready to use.
interpreter = tf.lite.Interpreter(model_content=tflite_model)
signature_defs = interpreter.get_signature_list()
self.assertLen(signature_defs, 3)
add_signature_runner = interpreter.get_signature_runner('add')
sub_signature_runner = interpreter.get_signature_runner('sub')
mul_signature_runner = interpreter.get_signature_runner('mul')
self.assertIsNotNone(add_signature_runner)
self.assertIsNotNone(sub_signature_runner)
self.assertIsNotNone(mul_signature_runner)
