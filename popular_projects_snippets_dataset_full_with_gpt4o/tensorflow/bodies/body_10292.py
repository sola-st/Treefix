# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
np.random.seed(1)
x_val = np.random.random_sample(x_shape).astype(x_dtype)
scale_val = np.random.random_sample(scale_shape).astype(scale_dtype)
offset_val = np.random.random_sample(scale_shape).astype(scale_dtype)

with self.cached_session(use_gpu=use_gpu):
    x = constant_op.constant(x_val, name='x')
    scale = constant_op.constant(scale_val, name='scale')
    offset = constant_op.constant(offset_val, name='offset')
    if is_training and exponential_avg_factor == 1.0:
        pop_mean = None
        pop_var = None
    else:
        pop_mean = np.random.random_sample(scale_shape).astype(scale_dtype)
        pop_var = np.random.random_sample(scale_shape).astype(scale_dtype)
    y, _, _ = nn_impl.fused_batch_norm(
        x,
        scale,
        offset,
        mean=pop_mean,
        variance=pop_var,
        exponential_avg_factor=exponential_avg_factor,
        data_format=data_format,
        is_training=is_training)
    if x_dtype not in [np.float16, dtypes.bfloat16.as_numpy_dtype]:
        err_x = gradient_checker.compute_gradient_error(x, x_shape, y, x_shape)
        err_scale = gradient_checker.compute_gradient_error(
            scale, scale_shape, y, x_shape)
        err_offset = gradient_checker.compute_gradient_error(
            offset, scale_shape, y, x_shape)
    else:
        x32 = constant_op.constant(x_val, name='x32', dtype=dtypes.float32)
        y32, _, _ = nn_impl.fused_batch_norm(
            x32,
            scale,
            offset,
            mean=pop_mean,
            variance=pop_var,
            data_format=data_format,
            exponential_avg_factor=exponential_avg_factor,
            is_training=is_training)
        err_x = self._compute_gradient_error_float16(x, x32, x_shape, y, y32,
                                                     x_shape, x_dtype)
        err_scale = self._compute_gradient_error_float16(
            scale, scale, scale_shape, y, y32, x_shape, x_dtype)
        err_offset = self._compute_gradient_error_float16(
            offset, offset, scale_shape, y, y32, x_shape, x_dtype)

x_err_tolerance = 1e-3
if x_dtype == np.float16:
    x_err_tolerance = 2e-3
elif dtypes.bfloat16.as_numpy_dtype:
    x_err_tolerance = 2e-2
scale_err_tolerance = 1e-3
self.assertLess(err_x, x_err_tolerance)
self.assertLess(err_scale, scale_err_tolerance)
self.assertLess(err_offset, scale_err_tolerance)
