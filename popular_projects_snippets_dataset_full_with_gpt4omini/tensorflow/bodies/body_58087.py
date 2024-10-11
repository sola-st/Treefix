# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
interpreter = interpreter_wrapper.Interpreter(
    model_path=resource_loader.get_path_to_datafile(
        'testdata/permute_float.tflite'))
interpreter.allocate_tensors()
# Invalid tensor index passed.
with self.assertRaisesRegex(ValueError, 'Tensor with no shape found.'):
    interpreter._get_tensor_details(4, 0)
with self.assertRaisesRegex(ValueError, 'Invalid node index'):
    interpreter._get_op_details(4)
