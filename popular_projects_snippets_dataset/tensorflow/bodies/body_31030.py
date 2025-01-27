# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/relu_op_test.py
self.assertAllClose(
    np.array([[-9.0, 0.7, -5.0, 0.3, -0.1], [0.1, -3.0, 0.5, -27.0, 0.9]]),
    nn_ops.leaky_relu(
        np.array([[-0.9, 0.7, -0.5, 0.3, -0.01],
                  [0.1, -0.3, 0.5, -2.7, 0.9]]),
        alpha=10))
self.assertAllClose(
    np.array([[9.0, 0.7, 5.0, 0.3, 0.1], [0.1, 3.0, 0.5, 27.0, 0.9]]),
    nn_ops.leaky_relu(
        np.array([[-0.9, 0.7, -0.5, 0.3, -0.01],
                  [0.1, -0.3, 0.5, -2.7, 0.9]]),
        alpha=-10))
