# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_d9m_test.py
if data_layout == 'channels_first':
    exit('NCHW')
elif data_layout == 'channels_last':
    exit('NHWC')
else:
    raise ValueError('Unknown data_layout')
