# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
tf_crelu = nn_ops.crelu(
    np.array([[-9, 7, -5, 3, -1], [1, -3, 5, -7, 9]]), axis=1)
np_crelu = np.array([[0, 7, 0, 3, 0, 9, 0, 5, 0, 1],
                     [1, 0, 5, 0, 9, 0, 3, 0, 7, 0]])
self.assertAllEqual(np_crelu, tf_crelu)
