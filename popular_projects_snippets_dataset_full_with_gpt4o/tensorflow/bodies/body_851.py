# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/extract_image_patches_op_test.py
"""Test for 2x2 kernel with 2x2 dilation."""
# [1, 2, 2, 1]
image = np.arange(16).reshape(1, 4, 4, 1).astype(np.float32)
# [1, 2, 2, 4]
patches = [[[[0, 2, 8, 10], [1, 3, 9, 11]],
            [[4, 6, 12, 14], [5, 7, 13, 15]]]]
self._VerifyValues(
    image,
    ksizes=[2, 2],
    strides=[1, 1],
    rates=[2, 2],
    padding="VALID",
    patches=patches)
