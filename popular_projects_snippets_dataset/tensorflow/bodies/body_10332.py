# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
with context.eager_mode():
    y_backprop = array_ops.ones((2, 2, 2, 3))
    x = array_ops.ones((2, 2, 2, 2))
    scale = array_ops.ones((2,))
    reserve_space_1 = array_ops.ones((2,))
    reserve_space_2 = array_ops.ones((2,))
    with self.assertRaisesRegex(errors_impl.InvalidArgumentError,
                                'x and y_backprop must have same shape,'):
        gen_nn_ops.fused_batch_norm_grad_v2(y_backprop, x, scale,
                                            reserve_space_1, reserve_space_2)

    y_backprop = array_ops.ones((2, 2, 2, 2))
    x = array_ops.ones((2, 2, 2, 2))
    scale = array_ops.ones((3,))
    reserve_space_1 = array_ops.ones((2,))
    reserve_space_2 = array_ops.ones((2,))
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        'scale must have the same number of elements'):
        gen_nn_ops.fused_batch_norm_grad_v2(y_backprop, x, scale,
                                            reserve_space_1, reserve_space_2)

    y_backprop = array_ops.ones((2, 2, 2, 2))
    x = array_ops.ones((2, 2, 2, 2))
    scale = array_ops.ones((2,))
    reserve_space_1 = array_ops.ones((3,))
    reserve_space_2 = array_ops.ones((2,))
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        'reserve_space_1 must have the same number of elements'):
        gen_nn_ops.fused_batch_norm_grad_v2(y_backprop, x, scale,
                                            reserve_space_1, reserve_space_2)

    y_backprop = array_ops.ones((2, 2, 2, 2))
    x = array_ops.ones((2, 2, 2, 2))
    scale = array_ops.ones((2,))
    reserve_space_1 = array_ops.ones((2,))
    reserve_space_2 = array_ops.ones((3,))
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        'reserve_space_2 must have the same number of elements'):
        gen_nn_ops.fused_batch_norm_grad_v2(y_backprop, x, scale,
                                            reserve_space_1, reserve_space_2)
