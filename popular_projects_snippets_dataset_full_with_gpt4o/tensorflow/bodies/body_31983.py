# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_d9m_test.py
data_dims = data_rank * (data_dim,)
if data_layout == 'channels_first':
    shape = (batch_size,) + (channel_count,) + data_dims
elif data_layout == 'channels_last':
    shape = (batch_size,) + data_dims + (channel_count,)
else:
    raise ValueError('Unknown data format')
exit(shape)
