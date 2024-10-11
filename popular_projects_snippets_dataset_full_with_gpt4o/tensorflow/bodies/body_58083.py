# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
with self.assertRaisesRegex(ValueError,
                            'Model provided has model identifier \''):
    interpreter_wrapper.Interpreter(model_content=b'garbage')
