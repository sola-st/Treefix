# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/check_ops_test.py
ten = sparse_tensor.SparseTensor(
    indices=[[0, 0], [1, 2]], values=[1, 2], dense_shape=[3, 4])
with self.assertRaisesRegex(TypeError, "proper"):
    check_ops.assert_proper_iterable(ten)
