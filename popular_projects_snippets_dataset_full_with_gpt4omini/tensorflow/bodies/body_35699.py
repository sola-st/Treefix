# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
"""Tests full-range int uniform.
    """
shape = [3, 4]
dtype = dtypes.int32
g = random.Generator.from_seed(1)
r1 = g.uniform(shape=shape, dtype=dtype, minval=None)
g = random.Generator.from_seed(1)
r2 = g.uniform_full_int(shape=shape, dtype=dtype)
self.assertAllEqual(r1, r2)
