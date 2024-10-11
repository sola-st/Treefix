# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
x_value = 5
rank_two_shapes = [(1, 1), (1, 3), ("a", "b"), (None, None)]
with ops.Graph().as_default():
    x = array_ops.placeholder(dtypes.float32, None)

    for shape in rank_two_shapes:
        regex = r"Tensor .* must have rank\] \[2\]"
        self.raises_dynamic_error(
            shapes=[(x, shape)], regex=regex, feed_dict={x: x_value})
