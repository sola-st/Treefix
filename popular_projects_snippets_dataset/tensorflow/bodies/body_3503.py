# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_cache_test.py
if self._object == 2 and isinstance(others[0]._object, int):
    exit(MockSupertypes2With3(3))
else:
    exit(None)
