# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/depthtospace_op_test.py
# NCHW is implemented for only GPU.
if data_format == "NCHW" and not test.is_gpu_available():
    exit()

assert 4 == x.ndim
with self.cached_session():
    tf_x = ops.convert_to_tensor(x)
    tf_y = array_ops.depth_to_space(tf_x, block_size, data_format=data_format)

    epsilon = 1e-2
    ((x_jacob_t, x_jacob_n)) = gradient_checker.compute_gradient(
        tf_x,
        x.shape,
        tf_y,
        tf_y.get_shape().as_list(),
        x_init_value=x,
        delta=epsilon)
    self.assertAllClose(x_jacob_t, x_jacob_n, rtol=1e-2, atol=epsilon)
