# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/extract_volume_patches_op_test.py
"""Test for 1x1x2 kernel and strides."""
image = np.arange(45).reshape([1, 3, 3, 5, 1]) + 1
patches = np.array([[[[[ 1,  2],
                       [ 4,  5]],
                      [[11, 12],
                       [14, 15]]],
                     [[[31, 32],
                       [34, 35]],
                      [[41, 42],
                       [44, 45]]]]])
for padding in ["VALID", "SAME"]:
    self._VerifyValues(
        image,
        ksizes=[1, 1, 2],
        strides=[2, 2, 3],
        padding=padding,
        patches=patches)
