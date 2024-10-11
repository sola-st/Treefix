# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/extract_image_patches_op_test.py
"""Test for 2x2 kernel with SAME padding."""
# [1, 2, 2, 1]
image = [[[[1], [2]], [[3], [4]]]]
# [1, 2, 2, 4]
patches = [[[[1, 2, 3, 4], [2, 0, 4, 0]], [[3, 4, 0, 0], [4, 0, 0, 0]]]]
self._VerifyValues(
    image,
    ksizes=[2, 2],
    strides=[1, 1],
    rates=[1, 1],
    padding="SAME",
    patches=patches)
