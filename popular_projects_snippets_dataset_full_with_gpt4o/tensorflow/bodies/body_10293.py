# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
np.random.seed(1)
x_val = np.random.random_sample(x_shape).astype(x_dtype)
grad_y_val = np.random.random_sample(x_shape).astype(x_dtype)
scale_val = np.random.random_sample(scale_shape).astype(scale_dtype)
offset_val = np.random.random_sample(scale_shape).astype(scale_dtype)

with self.cached_session(use_gpu=use_gpu) as sess:
    x = constant_op.constant(x_val, name='x')
    grad_y = constant_op.constant(grad_y_val, name='grad_y')
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
    grad_x, grad_scale, grad_offset = gradients_impl.gradients(
        y, [x, scale, offset], grad_y)

    if is_training:
        epsilon = y.op.get_attr('epsilon')
        data_format = y.op.get_attr('data_format')
        grad_vals = self.evaluate([grad_x, grad_scale, grad_offset])
        grad_internal = nn_grad._BatchNormGrad(grad_y, x, scale, pop_mean,
                                               pop_var, epsilon, data_format)
        grad_internal_vals = self.evaluate(list(grad_internal))
        for grad_val, grad_internal_val in zip(grad_vals, grad_internal_vals):
            self.assertAllClose(grad_val, grad_internal_val, atol=err_tolerance)

    if x_dtype not in [np.float16, dtypes.bfloat16.as_numpy_dtype]:
        err_grad_grad_y_1 = gradient_checker.compute_gradient_error(
            grad_y, x_shape, grad_x, x_shape)
        err_grad_grad_y_2 = gradient_checker.compute_gradient_error(
            grad_y, x_shape, grad_scale, scale_shape)
        err_grad_grad_y_3 = gradient_checker.compute_gradient_error(
            grad_y, x_shape, grad_offset, scale_shape)
        # In freeze mode, grad_x is not a function of x.
        if is_training:
            err_grad_x_1 = gradient_checker.compute_gradient_error(
                x, x_shape, grad_x, x_shape)
        err_grad_x_2 = gradient_checker.compute_gradient_error(
            x, x_shape, grad_scale, scale_shape)

        err_grad_scale = gradient_checker.compute_gradient_error(
            scale, scale_shape, grad_x, x_shape)
    else:
        x32 = constant_op.constant(x_val, dtype=dtypes.float32, name='x32')
        grad_y32 = constant_op.constant(
            grad_y_val, dtype=dtypes.float32, name='grad_y32')
        y32, _, _ = nn_impl.fused_batch_norm(
            x32,
            scale,
            offset,
            mean=pop_mean,
            variance=pop_var,
            exponential_avg_factor=exponential_avg_factor,
            data_format=data_format,
            is_training=is_training)
        grad_x32, grad_scale32, grad_offset32 = gradients_impl.gradients(
            y32, [x32, scale, offset], grad_y32)
        err_grad_grad_y_1 = self._compute_gradient_error_float16(
            grad_y, grad_y32, x_shape, grad_x, grad_x32, x_shape, x_dtype)
        err_grad_grad_y_2 = self._compute_gradient_error_float16(
            grad_y, grad_y32, x_shape, grad_scale, grad_scale32, scale_shape,
            x_dtype)
        err_grad_grad_y_3 = self._compute_gradient_error_float16(
            grad_y, grad_y32, x_shape, grad_offset, grad_offset32, scale_shape,
            x_dtype)
        # In freeze mode, grad_x is not a function of x.
        if is_training:
            err_grad_x_1 = self._compute_gradient_error_float16(
                x, x32, x_shape, grad_x, grad_x32, x_shape, x_dtype)
        err_grad_x_2 = self._compute_gradient_error_float16(
            x, x32, x_shape, grad_scale, grad_scale32, scale_shape, x_dtype)

        err_grad_scale = self._compute_gradient_error_float16(
            scale, scale, scale_shape, grad_x, grad_x32, x_shape, x_dtype)

self.assertLess(err_grad_grad_y_1, err_tolerance)
self.assertLess(err_grad_grad_y_2, err_tolerance)
self.assertLess(err_grad_grad_y_3, err_tolerance)
if is_training:
    self.assertLess(err_grad_x_1, err_tolerance)
self.assertLess(err_grad_x_2, err_tolerance)
self.assertLess(err_grad_scale, err_tolerance)
