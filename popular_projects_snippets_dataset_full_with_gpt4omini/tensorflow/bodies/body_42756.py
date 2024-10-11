# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/tensor_test.py
t = constant_op.constant(1., shape=[1] * 33)
with self.assertRaisesRegex(
    errors.InvalidArgumentError,
    "Cannot convert tensor with 33 dimensions to NumPy array. NumPy arrays "
    "can have at most 32 dimensions"):
    t.numpy()
