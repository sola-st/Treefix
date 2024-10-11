# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/random/stateful_random_ops_test.py
cp.write(fname)
r1 = g.uniform([], dtype=dtypes.uint32, minval=None)
cp.restore(fname)
r2 = g.uniform([], dtype=dtypes.uint32, minval=None)
self.assertAllEqual(r1, r2)
