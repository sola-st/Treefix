# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
with self.assertRaisesRegex(
    ValueError,
    "`output_shape` must be of length 3, 4 or 5.* of length 6."):
    nn_ops.conv_transpose(None, 2, [2, 3, 4, 2, 5, 1], "SAME")
