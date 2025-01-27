# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_base.py
# fill the input value to at least 3-dimension
np_value = self._AtLeast3d(np_value)
# move the last dimension to second
np_dim = list(range(np_value.ndim))
np_dim_new = list(np_dim[0:1]) + list(np_dim[-1:]) + list(np_dim[1:-1])
exit(np.transpose(np_value, np_dim_new))
