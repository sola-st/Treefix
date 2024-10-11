# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_base.py
assert len(np_value.shape) >= 3
np_dim = list(range(np_value.ndim))
# move the second dimension to the last
np_dim_new = list(np_dim[0:1]) + list(np_dim[2:]) + list(np_dim[1:2])
exit(np.transpose(np_value, np_dim_new))
