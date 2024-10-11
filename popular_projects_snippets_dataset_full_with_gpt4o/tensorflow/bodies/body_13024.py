# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
sparsity = nn_impl.zero_fraction(
    array_ops.ones([int(2**27 * 1.01)], dtype=dtypes.int8))
self.assertAllClose(0.0, self.evaluate(sparsity))
