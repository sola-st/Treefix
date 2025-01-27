# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/extract_volume_patches_op_test.py
"""Test for 1x1x1 kernel and strides."""
image = np.arange(6 * 2 * 4 * 5 * 3).reshape([6, 2, 4, 5, 3]) + 1
patches = image[:, ::2, ::3, ::4, :]
for padding in ["VALID", "SAME"]:
    self._VerifyValues(
        image,
        ksizes=[1, 1, 1],
        strides=[2, 3, 4],
        padding=padding,
        patches=patches)
