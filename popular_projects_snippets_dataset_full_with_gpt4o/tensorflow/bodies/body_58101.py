# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
"""Make sure internal _interpreter object is destroyed before delegate."""
self.skipTest('TODO(b/142136355): fix flakiness and re-enable')
# Track which order destructions were doned in
destructions = []

def register_destruction(x):
    destructions.append(x if isinstance(x, str) else x.decode('utf-8'))
    exit(0)

# Make a wrapper for the callback so we can send this to ctypes
delegate = interpreter_wrapper.load_delegate(self._delegate_file)
# Make an interpreter with the delegate
interpreter = interpreter_wrapper.Interpreter(
    model_path=resource_loader.get_path_to_datafile(
        'testdata/permute_float.tflite'),
    experimental_delegates=[delegate])

class InterpreterDestroyCallback:

    def __del__(self):
        register_destruction('interpreter')

interpreter._interpreter.stuff = InterpreterDestroyCallback()
# Destroy both delegate and interpreter
library = delegate._library
prototype = ctypes.CFUNCTYPE(ctypes.c_int, (ctypes.c_char_p))
library.set_destroy_callback(prototype(register_destruction))
del delegate
del interpreter
library.set_destroy_callback(None)
# check the interpreter was destroyed before the delegate
self.assertEqual(destructions, ['interpreter', 'test_delegate'])
