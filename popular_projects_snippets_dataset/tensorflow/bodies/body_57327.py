# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter.py
"""Loads delegate from the shared library.

    Args:
      library: Shared library name.
      options: Dictionary of options that are required to load the delegate. All
        keys and values in the dictionary should be serializable. Consult the
        documentation of the specific delegate for required and legal options.
        (default None)

    Raises:
      RuntimeError: This is raised if the Python implementation is not CPython.
    """

# TODO(b/136468453): Remove need for __del__ ordering needs of CPython
# by using explicit closes(). See implementation of Interpreter __del__.
if platform.python_implementation() != 'CPython':
    raise RuntimeError('Delegates are currently only supported into CPython'
                       'due to missing immediate reference counting.')

self._library = ctypes.pydll.LoadLibrary(library)
self._library.tflite_plugin_create_delegate.argtypes = [
    ctypes.POINTER(ctypes.c_char_p),
    ctypes.POINTER(ctypes.c_char_p), ctypes.c_int,
    ctypes.CFUNCTYPE(None, ctypes.c_char_p)
]
# The return type is really 'TfLiteDelegate*', but 'void*' is close enough.
self._library.tflite_plugin_create_delegate.restype = ctypes.c_void_p

# Convert the options from a dictionary to lists of char pointers.
options = options or {}
options_keys = (ctypes.c_char_p * len(options))()
options_values = (ctypes.c_char_p * len(options))()
for idx, (key, value) in enumerate(options.items()):
    options_keys[idx] = str(key).encode('utf-8')
    options_values[idx] = str(value).encode('utf-8')

class ErrorMessageCapture:

    def __init__(self):
        self.message = ''

    def report(self, x):
        self.message += x if isinstance(x, str) else x.decode('utf-8')

capture = ErrorMessageCapture()
error_capturer_cb = ctypes.CFUNCTYPE(None, ctypes.c_char_p)(capture.report)
# Do not make a copy of _delegate_ptr. It is freed by Delegate's finalizer.
self._delegate_ptr = self._library.tflite_plugin_create_delegate(
    options_keys, options_values, len(options), error_capturer_cb)
if self._delegate_ptr is None:
    raise ValueError(capture.message)
