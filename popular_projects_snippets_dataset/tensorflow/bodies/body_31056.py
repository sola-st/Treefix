# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
np_relu = np.maximum(np_features, np.zeros_like(np_features))
np_neg_relu = np.maximum(-np_features, np.zeros_like(np_features))
np_crelu = np.concatenate((np_relu, np_neg_relu),
                          len(np_features.shape) - 1)

tf_crelu = nn_ops.crelu(np_features)

self.assertAllClose(np_crelu, tf_crelu)
self.assertShapeEqual(np_crelu, tf_crelu)
