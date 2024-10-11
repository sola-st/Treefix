# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/lrn_ops_test.py
# Test for LRNGrad that compares against the CPU implementation.
shape = [1, 2, 3, 4]
total_size = np.prod(shape)
in_image_vals = np.arange(1, total_size + 1, dtype=np.float32)
out_image_vals = np.arange(1, total_size + 1, dtype=np.float32)
out_grads_vals = np.arange(1, total_size + 1, dtype=np.float32)
depth_radius = np.random.randint(1, shape[3])
bias = 1.0 + np.random.rand()
alpha = 1.0 * np.random.rand()
beta = 1.0 * np.random.rand()

with self.session():
    in_image = constant_op.constant(in_image_vals, shape=shape)
    out_image = constant_op.constant(out_image_vals, shape=shape)
    out_grads = constant_op.constant(out_grads_vals, shape=shape)
    with ops.device(CPU_DEVICE):
        expected = gen_nn_ops.lrn_grad(out_grads, in_image, out_image,
                                       depth_radius, bias, alpha, beta)
    with self.test_scope():
        actual = gen_nn_ops.lrn_grad(out_grads, in_image, out_image,
                                     depth_radius, bias, alpha, beta)
    expected_val = self.evaluate(expected)
    actual_val = self.evaluate(actual)
self.assertAllClose(actual_val, expected_val, rtol=1e-3)
