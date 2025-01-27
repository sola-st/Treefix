# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/extract_image_patches_op_test.py
"""Test for complex data types"""
for dtype in [np.complex64, np.complex128]:
    image = (
        np.reshape(range(120), [2, 3, 4, 5]).astype(dtype) +
        np.reshape(range(120, 240), [2, 3, 4, 5]).astype(dtype) * 1j)
    patches = (
        np.reshape(range(120), [2, 3, 4, 5]).astype(dtype) +
        np.reshape(range(120, 240), [2, 3, 4, 5]).astype(dtype) * 1j)
    for padding in ["VALID", "SAME"]:
        self._VerifyValues(
            image,
            ksizes=[1, 1],
            strides=[1, 1],
            rates=[1, 1],
            padding=padding,
            patches=patches)
