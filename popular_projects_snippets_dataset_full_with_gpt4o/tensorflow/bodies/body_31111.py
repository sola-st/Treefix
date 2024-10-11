# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv2d_transpose_test.py
# Test case for 8972
initializer = random_ops.truncated_normal(
    [3, 3, 5, 1], mean=0.0, stddev=0.01, dtype=dtypes.float32)
x = variables.Variable(random_ops.random_normal([3, 10, 5, 1]))
f = variable_scope.get_variable("f", initializer=initializer)
f_shape = array_ops.stack([array_ops.shape(x)[0], 10, 5, 5])
output = nn_ops.conv2d_transpose(
    x, f, f_shape, strides=[1, 1, 1, 1], padding="SAME")
self.assertEqual(output.get_shape().as_list(), [3, 10, 5, 5])
