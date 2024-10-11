# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/batchtospace_op_test.py
block_shape = np.array(block_shape)
crops = constant_op.constant(
    np.array(crops).reshape((len(block_shape), 2)), crops_dtype)
with self.cached_session():
    tf_x = ops.convert_to_tensor(x)
    tf_y = array_ops.batch_to_space_nd(tf_x, block_shape, crops)
    epsilon = 1e-5
    ((x_jacob_t, x_jacob_n)) = gradient_checker.compute_gradient(
        tf_x,
        x.shape,
        tf_y,
        tf_y.get_shape().as_list(),
        x_init_value=x,
        delta=epsilon)

self.assertAllClose(x_jacob_t, x_jacob_n, rtol=1e-2, atol=epsilon)
