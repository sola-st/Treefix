# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
# All shapes unknown.
c1 = nn_ops.conv2d(
    array_ops.placeholder(dtypes.float32),
    array_ops.placeholder(dtypes.float32),
    strides=[1, 1, 1, 1],
    padding="SAME")
self.assertEqual([None, None, None, None], c1.get_shape().as_list())

# Incorrect input shape.
with self.assertRaises(ValueError):
    nn_ops.conv2d(
        array_ops.placeholder(
            dtypes.float32, shape=[1, 3]),
        array_ops.placeholder(dtypes.float32),
        strides=[1, 1, 1, 1],
        padding="SAME")

# Incorrect filter shape.
with self.assertRaises(ValueError):
    nn_ops.conv2d(
        array_ops.placeholder(dtypes.float32),
        array_ops.placeholder(
            dtypes.float32, shape=[1, 3]),
        strides=[1, 1, 1, 1],
        padding="SAME")

# Depth mismatch.
with self.assertRaises(ValueError):
    nn_ops.conv2d(
        array_ops.placeholder(
            dtypes.float32, shape=[32, 20, 20, 3]),
        array_ops.placeholder(
            dtypes.float32, shape=[4, 4, 2, 2]),
        strides=[1, 1, 1, 1],
        padding="SAME")

# Input depth divisible by filter depth (group convolution).
# No exceptions should appear.
nn_ops.conv2d(
    array_ops.placeholder(dtypes.float32, shape=[32, 20, 20, 8]),
    array_ops.placeholder(dtypes.float32, shape=[4, 4, 2, 16]),
    strides=[1, 1, 1, 1],
    padding="SAME")

# Negative padding.
with self.assertRaises(ValueError):
    nn_ops.conv2d(
        array_ops.placeholder(dtypes.float32),
        array_ops.placeholder(dtypes.float32),
        strides=[1, 1, 1, 1],
        padding=[[0, 0], [0, -1], [1, 2], [0, 0]])

# Nonzero padding in nonspatial dimension.
with self.assertRaises(ValueError):
    nn_ops.conv2d(
        array_ops.placeholder(dtypes.float32),
        array_ops.placeholder(dtypes.float32),
        strides=[1, 1, 1, 1],
        padding=[[1, 0], [0, 0], [0, 0], [0, 0]])

# Nonzero NCHW padding in nonspatial dimension.
with self.assertRaises(ValueError):
    nn_ops.conv2d(
        array_ops.placeholder(dtypes.float32),
        array_ops.placeholder(dtypes.float32),
        strides=[1, 1, 1, 1],
        padding=[[0, 0], [0, 1], [0, 0], [0, 0]],
        data_format="NCHW")

# Wrong amount of padding
with self.assertRaises(ValueError):
    nn_ops.conv2d(
        array_ops.placeholder(dtypes.float32),
        array_ops.placeholder(dtypes.float32),
        strides=[1, 1, 1, 1],
        padding=[[0, 0], [0, 0], [0, 0]])

# Only specify one padding amount per dimension
with self.assertRaises(ValueError):
    nn_ops.conv2d(
        array_ops.placeholder(dtypes.float32),
        array_ops.placeholder(dtypes.float32),
        strides=[1, 1, 1, 1],
        padding=[[0], [0], [0], [0]])

# Explicit padding elements are not lists
with self.assertRaises(ValueError):
    nn_ops.conv2d(
        array_ops.placeholder(dtypes.float32),
        array_ops.placeholder(dtypes.float32),
        strides=[1, 1, 1, 1],
        padding=[0, 0, 0, 0])
