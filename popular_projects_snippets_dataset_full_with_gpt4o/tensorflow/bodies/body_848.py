# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/extract_image_patches_op_test.py
"""Test for 1x1 kernel and strides."""
# [2, 4, 5, 3]
image = np.reshape(range(120), [2, 4, 5, 3])
# [2, 2, 2, 3]
patches = image[:, ::2, ::3, :]
for padding in ["VALID", "SAME"]:
    self._VerifyValues(
        image,
        ksizes=[1, 1],
        strides=[2, 3],
        rates=[1, 1],
        padding=padding,
        patches=patches)
