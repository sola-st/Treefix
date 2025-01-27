# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
x_shape = [5, 17]
x_np = np.random.randint(0, 2, size=x_shape).astype(np.float32)
y_np = self._ZeroFraction(x_np)

x_tf = constant_op.constant(x_np)
x_tf.set_shape(x_shape)
y_tf = nn_impl.zero_fraction(x_tf)
y_tf_np = self.evaluate(y_tf)

eps = 1e-8
self.assertAllClose(y_tf_np, y_np, eps)
