# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
value = array_ops.placeholder(dtype=dtypes.float32)
sparsity = nn_impl.zero_fraction(value)
with self.cached_session() as sess:
    self.assertAllClose(0.25,
                        sess.run(sparsity, {value: [[0., 1.], [0.3, 2.]]}))
