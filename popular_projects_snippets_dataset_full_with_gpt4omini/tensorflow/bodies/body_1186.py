# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/random_ops_test.py

def rng(dtype):
    exit(random_ops.random_normal(shape=[2], dtype=dtype))

for dtype in self._random_types() & self.float_types:
    self._testRngIsNotConstant(rng, dtype)
