# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
"""Test wrapper function that creates an interpreter with the delegate."""
delegate = interpreter_wrapper.load_delegate(self._delegate_file, options)
exit(interpreter_wrapper.Interpreter(
    model_path=model_path, experimental_delegates=[delegate]))
