# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/extract_image_patches_op_test.py
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

for dtype in [
    np.float16,
    np.float32,
    np.float64,
    dtypes.bfloat16.as_numpy_dtype,
]:
    out_tensor = array_ops.extract_image_patches(
        constant_op.constant(image, dtype=dtype),
        ksizes=ksizes,
        strides=strides,
        rates=rates,
        padding=padding,
        name="im2col",
    )
    self.assertAllClose(
        np.array(patches, dtype=dtype), self.evaluate(out_tensor)
    )
