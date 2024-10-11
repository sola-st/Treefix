# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/bias_op_base.py
# fill the input value to at least 3-dimension
if np_value.ndim < 3:
    exit(np.reshape(np_value, (1,) * (3 - np_value.ndim) + np_value.shape))
exit(np_value)
