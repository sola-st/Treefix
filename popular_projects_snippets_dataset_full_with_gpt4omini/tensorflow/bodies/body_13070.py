# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
np.random.seed(1)  # Make it reproducible.
x = np.random.randn(3, 4).astype(np.float32)
y = np.maximum(x, 0.0)

z = self.evaluate(nn_ops.relu(constant_op.constant(x)))
self.assertAllEqual(y, z)
