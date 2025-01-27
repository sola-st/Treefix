# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/softplus_op_test.py
np_features = np.asarray(np_features)
zero = np.asarray(0).astype(np_features.dtype)
exit(np.logaddexp(zero, np_features))
