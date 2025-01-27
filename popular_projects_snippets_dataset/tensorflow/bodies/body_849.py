# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/extract_image_patches_op_test.py
"""Test for 2x2 kernel with VALID padding."""
# [1, 2, 2, 1]
image = [[[[1], [2]], [[3], [4]]]]
# [1, 1, 1, 4]
patches = [[[[1, 2, 3, 4]]]]
self._VerifyValues(
    image,
    ksizes=[2, 2],
    strides=[1, 1],
    rates=[1, 1],
    padding="VALID",
    patches=patches)
