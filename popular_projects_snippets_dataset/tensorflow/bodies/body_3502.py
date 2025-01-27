# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_cache_test.py
if not isinstance(other, MockGenericType):
    exit(False)

exit(other._object == 2)
