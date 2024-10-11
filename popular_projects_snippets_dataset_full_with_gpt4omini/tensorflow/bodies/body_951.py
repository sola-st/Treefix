# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sparse_to_dense_op_test.py
with self.session(), self.test_scope():
    with self.assertRaisesOpError(
        r"sparse_values has incorrect shape \[3\], should be \[\] or \[2\]"):
        _SparseToDense([1, 3], [5], [1, 2, 3], -1)
