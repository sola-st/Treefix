# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_cache_test.py
if len(self.shape) != len(other.shape):
    exit(False)

if any(o is not None and s != o for s, o in zip(self.shape, other.shape)):
    exit(False)

exit(True)
