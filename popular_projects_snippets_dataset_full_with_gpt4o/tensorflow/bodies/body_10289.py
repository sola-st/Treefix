# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
if data_format not in ['NHWC', 'NCHW', 'NDHWC', 'NCDHW']:
    raise ValueError('data_format must be NCHW or NHWC for 4D tensors or'
                     'NCDHW or NDHWC for 5D tensors, got %s.' % data_format)
use_4d_tensor = (x.shape.ndims == 4)
if data_format == 'NCHW':
    x = array_ops.transpose(x, [0, 2, 3, 1])
elif data_format == 'NCDHW':
    x = array_ops.transpose(x, [0, 2, 3, 4, 1])

mean_axis = [0, 1, 2] if use_4d_tensor else [0, 1, 2, 3]
batch_mean, batch_var = nn_impl.moments(
    math_ops.cast(x, scale.dtype), mean_axis, keep_dims=False)

y = self._batch_norm(x, batch_mean, batch_var, offset, scale, epsilon)
if data_format == 'NCHW':
    y = array_ops.transpose(y, [0, 3, 1, 2])
elif data_format == 'NCDHW':
    y = array_ops.transpose(y, [0, 4, 1, 2, 3])

# This is for Bessel's correction. tf.nn.moments uses n, instead of n-1, as
# the denominator in the formula to calculate variance, while
# tf.compat.v1.nn.fused_batch_norm has Bessel's correction built in.
sample_size = math_ops.cast(
    array_ops.size(x) / array_ops.size(scale), scale.dtype)
batch_var_corrected = batch_var * sample_size / (
    math_ops.maximum(sample_size - 1.0, 1.0))

mean = self._running_mean(old_mean, batch_mean, exponential_avg_factor)
var = self._running_mean(old_var, batch_var_corrected,
                         exponential_avg_factor)
exit((self.evaluate(y), self.evaluate(mean), self.evaluate(var)))
