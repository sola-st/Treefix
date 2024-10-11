# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_3d_test.py
expected_output = [2., 5., 8., 18., 21., 24., 34., 37., 40.]
self._VerifyValues(
    nn_ops.max_pool3d,
    input_sizes=[1, 5, 8, 1, 1],
    window=(1, 2, 3),
    strides=(2, 3, 1),
    padding="SAME",
    expected=expected_output)

# Test pooling on a larger input, with different stride and kernel
# size for the 'z' dimension.

# Simulate max pooling in numpy to get the expected output.
input_data = np.arange(1, 5 * 27 * 27 * 64 + 1).reshape((5, 27, 27, 64))
input_data = np.pad(input_data, [[0, 0], [0, 1], [0, 1], [0, 0]],
                    mode="constant")
expected_output = input_data[:, 1::2, 1::2, :]
expected_output[:, -1, :, :] = input_data[:, -2, 1::2, :]
expected_output[:, :, -1, :] = input_data[:, 1::2, -2, :]
expected_output[:, -1, -1, :] = input_data[:, -2, -2, :]

self._VerifyValues(
    nn_ops.max_pool3d,
    input_sizes=[1, 5, 27, 27, 64],
    window=(1, 2, 2),
    strides=(1, 2, 2),
    padding="SAME",
    expected=expected_output.flatten())
