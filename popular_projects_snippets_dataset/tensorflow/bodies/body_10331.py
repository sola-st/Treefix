# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
with context.eager_mode():
    x = array_ops.ones((2, 2, 2, 2))
    scale = array_ops.ones((3,))
    offset = array_ops.ones((2,))
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        'scale must have the same number of elements'):
        nn_impl.fused_batch_norm(x, scale, offset)

    x = array_ops.ones((2, 2, 2, 2))
    scale = array_ops.ones((2,))
    offset = array_ops.ones((3,))
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        'offset must have the same number of elements'):
        nn_impl.fused_batch_norm(x, scale, offset)

    x = array_ops.ones((2, 2, 2, 2))
    scale = array_ops.ones((2,))
    offset = array_ops.ones((2,))
    mean = array_ops.ones((0,))
    variance = array_ops.ones((2,))
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        'When is_training=false, mean must have the same number of elements'):
        nn_impl.fused_batch_norm(
            x, scale, offset, mean=mean, variance=variance, is_training=False)

    x = array_ops.ones((2, 2, 2, 2))
    scale = array_ops.ones((2,))
    offset = array_ops.ones((2,))
    mean = array_ops.ones((2,))
    variance = array_ops.ones((0,))
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        'When is_training=false, variance must have the same number of '
        'elements'):
        nn_impl.fused_batch_norm(
            x, scale, offset, mean=mean, variance=variance, is_training=False)

    x = array_ops.ones((2, 2, 2, 2))
    scale = array_ops.ones((2,))
    offset = array_ops.ones((2,))
    mean = array_ops.ones((0,))
    variance = array_ops.ones((2,))
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        'When exponential_avg_factor != 1, mean must have the same number of '
        'elements'):
        nn_impl.fused_batch_norm(
            x,
            scale,
            offset,
            mean=mean,
            variance=variance,
            exponential_avg_factor=0.5)

    x = array_ops.ones((2, 2, 2, 2))
    scale = array_ops.ones((2,))
    offset = array_ops.ones((2,))
    mean = array_ops.ones((2,))
    variance = array_ops.ones((0,))
    with self.assertRaisesRegex(
        errors_impl.InvalidArgumentError,
        'When exponential_avg_factor != 1, variance must have the same '
        'number of elements'):
        nn_impl.fused_batch_norm(
            x,
            scale,
            offset,
            mean=mean,
            variance=variance,
            exponential_avg_factor=0.5)
