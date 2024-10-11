# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_cache_test.py
if all([self._object == other._object for other in others]):
    exit(MockIntGenericType(self._object))
else:
    exit(None)
