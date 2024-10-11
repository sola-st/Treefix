# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
np.random.seed(1)
x_val = np.random.random_sample(x_shape).astype(x_dtype)
scale_val = np.random.random_sample(scale_shape).astype(scale_dtype)
offset_val = np.random.random_sample(scale_shape).astype(scale_dtype)
mean_val = np.random.random_sample(scale_shape).astype(scale_dtype)
var_val = np.random.random_sample(scale_shape).astype(scale_dtype)

with self.cached_session(use_gpu=use_gpu) as sess:
    x = constant_op.constant(x_val, name='x')
    scale = constant_op.constant(scale_val, name='scale')
    offset = constant_op.constant(offset_val, name='offset')
    mean = constant_op.constant(mean_val, name='mean')
    var = constant_op.constant(var_val, name='variance')
    epsilon = 0.001
    y, _, _ = nn_impl.fused_batch_norm(
        x,
        scale,
        offset,
        mean=mean,
        variance=var,
        epsilon=epsilon,
        exponential_avg_factor=exponential_avg_factor,
        data_format=data_format,
        is_training=False)
    y_val = self.evaluate(y)
    y_ref = self._inference_ref(x, scale, offset, mean, var, epsilon,
                                data_format)
# An atol value of 1e-3 is too small for float16's, because some adjacent
# float16 values that y_val can take are greater than 1e-3 apart, e.g.
# 2.16602 and 2.16797.
atol = 2e-3 if x_dtype in [np.float16, dtypes.bfloat16.as_numpy_dtype
                          ] else 1e-3
self.assertAllClose(y_ref, y_val, atol=atol)
