# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/random_ops_test.py
for dtype in self._random_types():
    # TODO (b/112272078): enable bfloat16 for CPU and GPU when the bug is
    # fixed.
    if (self.device in ['XLA_GPU', 'XLA_CPU'
                       ]) and (dtype in [dtypes.bfloat16, dtypes.half]):
        continue
    with self.session():
        with self.test_scope():
            x = random_ops.random_uniform(
                shape=[1000], dtype=dtype, minval=-2, maxval=33)
        y = self.evaluate(x)
        msg = str(y) + str(dtype)
        self.assertEqual((y >= -2).sum(), 1000, msg)
        self.assertEqual((y < 33).sum(), 1000, msg)
