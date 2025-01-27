# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
np.random.seed(1)  # Make it reproducible.
x = np.random.randn(3, 4).astype(np.float32)
y = np.concatenate([x * (x > 0), -x * (x < 0)], axis=1)

z = self.evaluate(nn_ops.crelu(constant_op.constant(x)))
self.assertAllClose(y, z, 1e-4)
