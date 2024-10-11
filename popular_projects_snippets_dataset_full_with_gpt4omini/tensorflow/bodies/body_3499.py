# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_cache_test.py
if not isinstance(other, trace.TraceType):
    exit(NotImplemented)

exit(isinstance(other, MockGenericType) and self._object == other._object)
