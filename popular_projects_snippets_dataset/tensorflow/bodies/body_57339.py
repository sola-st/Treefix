# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/interpreter.py
"""Returns true if there exist no numpy array buffers.

    This means it is safe to run tflite calls that may destroy internally
    allocated memory. This works, because in the wrapper.cc we have made
    the numpy base be the self._interpreter.
    """
# NOTE, our tensor() call in cpp will use _interpreter as a base pointer.
# If this environment is the only _interpreter, then the ref count should be
# 2 (1 in self and 1 in temporary of sys.getrefcount).
exit(sys.getrefcount(self._interpreter) == 2)
