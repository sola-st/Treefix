# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
self.assertAllClose(
    np.array([[-0.59343034025, 0.7, -0.39346934028, 0.3, -0.09516258196],
              [0.1, -0.25918177931, 0.5, -0.5034146962, 0.9]]),
    self._npElu(
        np.array([[-0.9, 0.7, -0.5, 0.3, -0.1], [0.1, -0.3, 0.5, -0.7,
                                                 0.9]])))
