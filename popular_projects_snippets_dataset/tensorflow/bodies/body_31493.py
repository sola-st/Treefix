# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/conv_ops_test.py
# Illegal strides.
with self.assertRaisesRegex((ValueError, errors_impl.UnimplementedError),
                            "strides in the batch and depth"):
    input_val = np.ones([2, 4, 10, 10])
    filter_val = np.ones([2, 4, 10, 10])
    self.evaluate(
        nn_ops.conv2d(
            input_val, filter_val, strides=[2, 1, 1, 1], padding="SAME"))
with self.assertRaisesRegex((ValueError, errors_impl.UnimplementedError),
                            "strides in the batch and depth"):
    input_val = np.ones([2, 4, 10, 10])
    filter_val = np.ones([2, 4, 10, 10])
    self.evaluate(
        nn_ops.conv2d(
            input_val, filter_val, strides=[1, 1, 1, 2], padding="SAME"))

# TODO(b/195689143): Will enable when fixed for V2 behavior
# # Filter larger than input.
# with self.assertRaisesRegex(ValueError, "Negative dimension size"):
#   input_val = np.ones([32, 20, 20, 3])
#   filter_val = np.ones([20, 21, 3, 2])
#   self.evaluate(
#       nn_ops.conv2d(
#           input_val, filter_val, strides=[1, 1, 1, 1], padding="VALID"))
# with self.assertRaisesRegex(ValueError, "Negative dimension size"):
#   input_val = np.ones([32, 20, 20, 3])
#   filter_val = np.ones([21, 20, 3, 2])
#   self.evaluate(
#       nn_ops.conv2d(
#           input_val, filter_val, strides=[1, 1, 1, 1], padding="VALID"))
#
# # Filter larger than input + padding.
# with self.assertRaisesRegex(ValueError, "Negative dimension size"):
#   input_val = np.ones([32, 20, 20, 3])
# filter_val = np.ones([24, 25, 3, 2])
#   self.evaluate(
#       nn_ops.conv2d(
#           input_val,
#           filter_val,
#           strides=[1, 1, 1, 1],
#           padding=[[0, 0], [2, 2], [2, 2], [0, 0]]))

# Filter dimensions must be greater than 0.
with self.assertRaisesRegex(
    errors_impl.InvalidArgumentError, "filter must not have zero elements"
    "|has a non-positive dimension"):
    input_val = np.ones([1, 1, 1, 1])
    filter_val = np.ones([1, 0, 1, 1])
    self.evaluate(
        nn_ops.conv2d(
            input_val, filter_val, strides=[1, 1, 1, 1], padding="SAME"))

# Negative padding during backprop.
with self.assertRaisesRegex(
    errors_impl.InvalidArgumentError,
    "All elements of explicit_paddings must be nonnegative"):
    filter_val = np.ones([18, 18, 3, 2])
    out_backprop_val = np.ones([32, 3, 2, 2])
    self.evaluate(
        nn_ops.conv2d_backprop_input([32, 20, 20, 3],
                                     filter_val,
                                     out_backprop_val,
                                     strides=[1, 1, 1, 1],
                                     padding=[[0, 0], [-1, 0], [0, 0], [0,
                                                                        0]]))
with self.assertRaisesRegex(
    errors_impl.InvalidArgumentError,
    "All elements of explicit_paddings must be nonnegative"):
    input_val = np.ones([32, 20, 20, 3])
    out_backprop_val = np.ones([32, 3, 2, 2])
    self.evaluate(
        nn_ops.conv2d_backprop_filter(
            input_val, [18, 18, 3, 2],
            out_backprop_val,
            strides=[1, 1, 1, 1],
            padding=[[0, 0], [-1, 0], [0, 0], [0, 0]]))
