# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
exit(np.where(np_features < 0, np.exp(np_features) - 1, np_features))
