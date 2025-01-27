# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/extract_image_patches_op_test.py
"""Test for 2x2 kernel with VALID padding."""
# [1, 2, 2, 2]
image = [[[[1, 5], [2, 6]], [[3, 7], [4, 8]]]]
# [1, 1, 1, 8]
patches = [[[[1, 5, 2, 6, 3, 7, 4, 8]]]]
self._VerifyValues(
    image,
    ksizes=[2, 2],
    strides=[1, 1],
    rates=[1, 1],
    padding="VALID",
    patches=patches)
