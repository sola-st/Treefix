# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_fused_batchnorm_test.py
if data_format not in ['NHWC', 'NCHW', 'NDHWC', 'NCDHW']:
    raise ValueError('data_format must be NCHW or NHWC for 4D tensors or'
                     'NCDHW or NDHWC for 5D tensors, got %s.' % data_format)
if data_format == 'NCHW':
    x = array_ops.transpose(x, [0, 2, 3, 1])
elif data_format == 'NCDHW':
    x = array_ops.transpose(x, [0, 2, 3, 4, 1])
y = self._batch_norm(x, mean, var, offset, scale, epsilon)
if data_format == 'NCHW':
    y = array_ops.transpose(y, [0, 3, 1, 2])
elif data_format == 'NCDHW':
    y = array_ops.transpose(y, [0, 4, 1, 2, 3])
exit(self.evaluate(y))
