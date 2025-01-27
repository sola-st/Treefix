# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
with self.cached_session():
    inp = np.random.rand(4, 2).astype("f")
    a = constant_op.constant(
        [float(x) for x in inp.flatten()], shape=[4, 2], dtype=dtypes.float32)
    tiled = array_ops.tile(a, [1, 2])
    grad_shape = [4, 4]
    grad_inp = np.random.rand(*grad_shape).astype("f")
    grad_tensor = constant_op.constant(
        [float(x) for x in grad_inp.flatten()], shape=grad_shape)
    grad = gradients_impl.gradients([tiled], [a], [grad_tensor])[0]
    self.assertShapeEqual(inp, grad)
    result = self.evaluate(grad)
expected_shape = [4, 2]
expected = np.zeros(expected_shape)
expected[:, 0] = grad_inp[:, 0] + grad_inp[:, 2]
expected[:, 1] = grad_inp[:, 1] + grad_inp[:, 3]
self.assertTrue((np.abs(expected - result) < 1e-3).all())
