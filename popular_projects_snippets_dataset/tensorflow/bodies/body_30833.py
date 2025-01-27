# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/lrn_op_test.py
depth_radius = 1
bias = 1.59018219
alpha = 0.117728651
beta = 0.404427052
input_grads = random_ops.random_uniform(
    shape=[4, 4, 4, 4],
    minval=-10000,
    maxval=10000,
    dtype=dtypes.float32,
    seed=-2033)
input_image = random_ops.random_uniform(
    shape=[4, 4, 4, 4],
    minval=-10000,
    maxval=10000,
    dtype=dtypes.float32,
    seed=-2033)
invalid_output_image = random_ops.random_uniform(
    shape=[4, 4, 4, 4, 4, 4],
    minval=-10000,
    maxval=10000,
    dtype=dtypes.float32,
    seed=-2033)
with self.assertRaises((ValueError, errors_impl.InvalidArgumentError)):
    self.evaluate(
        nn.lrn_grad(
            input_grads=input_grads,
            input_image=input_image,
            output_image=invalid_output_image,
            depth_radius=depth_radius,
            bias=bias,
            alpha=alpha,
            beta=beta))
