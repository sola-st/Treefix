# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
sixes = np.copy(np_features)
sixes.fill(6.0)
exit(np.minimum(
    np.maximum(np_features, np.zeros(np_features.shape)), sixes))
