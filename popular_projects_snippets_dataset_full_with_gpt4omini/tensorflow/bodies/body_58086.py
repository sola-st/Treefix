# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
with self.assertRaisesRegex(
    ValueError, '`model_path` or `model_content` must be specified.'):
    interpreter_wrapper.Interpreter(model_path=None, model_content=None)
