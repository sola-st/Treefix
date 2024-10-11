# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
with self.assertRaisesRegex(
    ValueError, "`output_shape` must be a tensor or sized collection"):
    nn_ops.conv_transpose(None, None, None, None)
