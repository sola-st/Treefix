# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
with self.assertRaisesRegex(ValueError,
                            'Could not open \'totally_invalid_file_name\''):
    interpreter_wrapper.Interpreter(model_path='totally_invalid_file_name')
