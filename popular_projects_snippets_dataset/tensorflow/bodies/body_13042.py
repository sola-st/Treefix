# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x_shape = [20, 7, 3]
np.random.seed(1)
x_np = np.random.random_sample(x_shape).astype(np.float32)
dim = [1, 2]
y_np = self._l2Normalize(x_np, dim)
x_tf = constant_op.constant(x_np, name="x")
y_tf = nn_impl.l2_normalize(x_tf, dim)
self.assertAllClose(y_np, self.evaluate(y_tf))
