# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/extract_image_patches_op_test.py
"""Tests input-output pairs for the ExtractImagePatches op.

    Args:
      image: Input tensor with shape: [batch, in_rows, in_cols, depth].
      ksizes: Patch size specified as: [ksize_rows, ksize_cols].
      strides: Output strides, specified as [stride_rows, stride_cols].
      rates: Atrous rates, specified as [rate_rows, rate_cols].
      padding: Padding type.
      patches: Expected output.
    """
ksizes = [1] + ksizes + [1]
strides = [1] + strides + [1]
rates = [1] + rates + [1]

with self.session():
    image_placeholder = array_ops.placeholder(dtypes.float32)
    with self.test_scope():
        out_tensor = array_ops.extract_image_patches(
            image_placeholder,
            ksizes=ksizes,
            strides=strides,
            rates=rates,
            padding=padding,
            name="im2col")
    feed_dict = {image_placeholder: image}
    self.assertAllClose(patches, out_tensor.eval(feed_dict=feed_dict))
