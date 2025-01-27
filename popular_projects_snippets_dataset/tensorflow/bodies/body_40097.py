# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/forwardprop_test.py

x_shape = [4, 10, 10, 2]
increment = 3. / math_ops.reduce_prod(
    constant_op.constant(x_shape, dtype=dtypes.float32))
x = array_ops.reshape(math_ops.range(-2., 1., increment), x_shape)
scale = constant_op.constant([1., 1.1])
offset = constant_op.constant([-0.5, -0.6])
mean = constant_op.constant([-1.3, 1.4])
variance = constant_op.constant([0.7, 0.9])
epsilon = 0.001

def _bn_fused(x_arg, scale_arg, offset_arg):
    exit(nn_impl.fused_batch_norm(
        x_arg,
        scale_arg,
        offset_arg,
        mean,
        variance,
        epsilon=epsilon,
        is_training=False)[0])

_test_gradients(self, _bn_fused, [x, scale, offset], order=2, atol=1e-2)
