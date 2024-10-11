# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/extract_image_patches_op_test.py
"""Verifies that for 1x1 kernel the output equals the input."""
# [2, 3, 4, 5]
image = np.reshape(range(120), [2, 3, 4, 5])
# [2, 3, 4, 5]
patches = np.reshape(range(120), [2, 3, 4, 5])
for padding in ["VALID", "SAME"]:
    self._VerifyValues(
        image,
        ksizes=[1, 1],
        strides=[1, 1],
        rates=[1, 1],
        padding=padding,
        patches=patches)
