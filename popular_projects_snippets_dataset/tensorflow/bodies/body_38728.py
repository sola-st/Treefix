# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/extract_volume_patches_op_test.py
"""Tests input-output pairs for the ExtractVolumePatches op.

    Args:
      image: Input tensor with shape:
             [batch, in_planes, in_rows, in_cols, depth].
      ksizes: Patch size specified as: [ksize_planes, ksize_rows, ksize_cols].
      strides: Output strides, specified as:
               [stride_planes, stride_rows, stride_cols].
      padding: Padding type.
      patches: Expected output.

    Note:
      rates are not supported as of now.
    """
ksizes = [1] + ksizes + [1]
strides = [1] + strides + [1]

for dtype in [
    np.float16,
    np.float32,
    np.float64,
    dtypes.bfloat16.as_numpy_dtype,
]:
    out_tensor = array_ops.extract_volume_patches(
        constant_op.constant(image.astype(dtype)),
        ksizes=ksizes,
        strides=strides,
        padding=padding,
        name="im2col_3d")
    self.assertAllClose(patches.astype(dtype), self.evaluate(out_tensor))
