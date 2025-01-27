# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter_test.py
super(InterpreterDelegateTest, self).setUp()
self._delegate_file = resource_loader.get_path_to_datafile(
    'testdata/test_delegate.so')
self._model_file = resource_loader.get_path_to_datafile(
    'testdata/permute_float.tflite')

# Load the library to reset the counters.
library = ctypes.pydll.LoadLibrary(self._delegate_file)
library.initialize_counters()
