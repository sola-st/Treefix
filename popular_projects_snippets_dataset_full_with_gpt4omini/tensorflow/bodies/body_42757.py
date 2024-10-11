# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
# Creating a Numpy array fails in some cases if the product of non-zero
# dimensions is very big, even if the shape also has a zero in it.
t = array_ops.ones((0, 2**31, 2**31))
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    r"Failed to create numpy array from tensor of shape "
    r"\[0, 2147483648, 2147483648\]. Numpy error.*array is too big"):
    t.numpy()
