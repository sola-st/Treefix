# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv3d_transpose_test.py
# Test case for GitHub issue 18460
x_shape = [2, 2, 3, 4, 3]
f_shape = [3, 3, 3, 2, 2]
y_shape = [2, 2, 6, 8, 6]
strides = [1, 1, 2, 2, 2]
np.random.seed(1)
x_value = np.random.random_sample(x_shape).astype(np.float64)
f_value = np.random.random_sample(f_shape).astype(np.float64)
nn_ops.conv3d_transpose(
    x_value, f_value, y_shape, strides, data_format="NCDHW")
