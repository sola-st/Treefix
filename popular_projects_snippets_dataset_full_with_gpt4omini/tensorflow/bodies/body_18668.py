# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_d9m_test.py
if large_batch:
    batch_size = 5000
    height = width = 4
else:
    batch_size = 10
    height = 5
    width = 5000
channel_count = 3
if data_format == 'NHWC':
    x_shape = (batch_size, height, width, channel_count)
else:  # 'NCHW'
    x_shape = (batch_size, channel_count, height, width)
# Using random_ops.random_normal would produce different values on each run
x = constant_op.constant(np.random.normal(size=x_shape), dtype=x_dtype)
scale_shape = (channel_count,)
scale = constant_op.constant(
    np.random.normal(size=scale_shape), dtype=dtypes.float32)
offset = constant_op.constant(
    np.random.normal(size=scale_shape), dtype=dtypes.float32)
mean = np.random.normal(size=scale_shape)
variance = np.random.normal(size=scale_shape)
y_shape = x_shape
y_dtype = x_dtype
upstream_gradients = constant_op.constant(
    np.random.normal(size=y_shape), dtype=y_dtype)
exit((x, scale, offset, mean, variance, upstream_gradients))
