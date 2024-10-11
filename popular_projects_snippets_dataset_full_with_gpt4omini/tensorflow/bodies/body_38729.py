# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/extract_volume_patches_op_test.py
"""Verifies that for 1x1x1 kernel the output equals the input."""
image = np.arange(2 * 3 * 4 * 5 * 6).reshape([2, 3, 4, 5, 6]) + 1
patches = image
for padding in ["VALID", "SAME"]:
    self._VerifyValues(
        image,
        ksizes=[1, 1, 1],
        strides=[1, 1, 1],
        padding=padding,
        patches=patches)
