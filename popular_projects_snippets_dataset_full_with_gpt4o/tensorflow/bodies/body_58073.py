# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
with self.assertRaisesRegex(
    ValueError, 'Unrecognized passed in op resolver type: test'):
    interpreter_wrapper.Interpreter(
        model_path=resource_loader.get_path_to_datafile(
            'testdata/permute_float.tflite'),
        experimental_op_resolver_type='test')
