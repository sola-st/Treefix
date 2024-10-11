# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter.py
# __del__ can not be called multiple times, so if the delegate is destroyed.
# don't try to destroy it twice.
if self._library is not None:
    self._library.tflite_plugin_destroy_delegate.argtypes = [ctypes.c_void_p]
    self._library.tflite_plugin_destroy_delegate(self._delegate_ptr)
    self._library = None
