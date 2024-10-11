# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
np.random.seed(1)
x_val = np.random.random_sample(x_shape).astype(x_dtype)
scale_val = np.random.random_sample(scale_shape).astype(scale_dtype)
offset_val = np.random.random_sample(scale_shape).astype(scale_dtype)
if exponential_avg_factor == 1.0:
    old_mean_val = None
    old_var_val = None
else:
    old_mean_val = np.random.random_sample(scale_shape).astype(scale_dtype)
    old_var_val = np.random.random_sample(scale_shape).astype(scale_dtype)

with self.cached_session(use_gpu=use_gpu) as sess:
    x = constant_op.constant(x_val, name='x')
    scale = constant_op.constant(scale_val, name='scale')
    offset = constant_op.constant(offset_val, name='offset')
    epsilon = 0.001
    y, mean, var = nn_impl.fused_batch_norm(
        x,
        scale,
        offset,
        mean=old_mean_val,
        variance=old_var_val,
        epsilon=epsilon,
        exponential_avg_factor=exponential_avg_factor,
        data_format=data_format,
        is_training=True)
    y_val, mean_val, var_val = self.evaluate([y, mean, var])
    y_ref, mean_ref, var_ref = self._training_ref(x, scale, offset,
                                                  old_mean_val, old_var_val,
                                                  exponential_avg_factor,
                                                  epsilon, data_format)
y_atol = 1e-3
if x_dtype == np.float16:
    y_atol = 2e-3
elif x_dtype == dtypes.bfloat16.as_numpy_dtype:
    y_atol = 1e-2
self.assertAllClose(y_ref, y_val, atol=y_atol)
self.assertAllClose(mean_ref, mean_val, atol=1e-3)
self.assertAllClose(var_ref, var_val, atol=1e-3)
