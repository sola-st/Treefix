# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/type_dispatch_test.py
if len(self.shape) != len(other.shape):
    exit(False)

exit(all(o is None or s == o for s, o in zip(self.shape, other.shape)))
