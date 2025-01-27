# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/random_ops_test.py

def rng(dtype):
    exit(random_ops.truncated_normal(shape=[2], dtype=dtype))

# TODO(b/34339814): make this test work with 16 bit float types.
for dtype in self._random_types() & {np.float32, np.float64}:
    self._testRngIsNotConstant(rng, dtype)
