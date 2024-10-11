# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/extract_volume_patches_op_test.py
"""Test for 2x2x2 kernel with SAME padding."""
image = np.arange(8).reshape([1, 2, 2, 2, 1]) + 1
patches = np.array([[[[[1, 2, 3, 4, 5, 6, 7, 8],
                       [2, 0, 4, 0, 6, 0, 8, 0]],
                      [[3, 4, 0, 0, 7, 8, 0, 0],
                       [4, 0, 0, 0, 8, 0, 0, 0]]],
                     [[[5, 6, 7, 8, 0, 0, 0, 0],
                       [6, 0, 8, 0, 0, 0, 0, 0]],
                      [[7, 8, 0, 0, 0, 0, 0, 0],
                       [8, 0, 0, 0, 0, 0, 0, 0]]]]])
self._VerifyValues(
    image,
    ksizes=[2, 2, 2],
    strides=[1, 1, 1],
    padding="SAME",
    patches=patches)
