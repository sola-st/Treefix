# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
with self.session():
    inp = np.random.rand(4, 1).astype("f")
    a = constant_op.constant(
        [float(x) for x in inp.flatten()], shape=[4, 1], dtype=dtypes.float32)
    tiled = array_ops.tile(a, [1, 4])
    grad_shape = [4, 4]
    grad_inp = np.random.rand(*grad_shape).astype("f")
    grad_tensor = constant_op.constant(
        [float(x) for x in grad_inp.flatten()], shape=grad_shape)
    grad = gradients_impl.gradients([tiled], [a], [grad_tensor])[0]
    result = self.evaluate(grad)
self.assertAllClose(np.sum(grad_inp, axis=1).reshape(4, 1), result, 1e-3)
