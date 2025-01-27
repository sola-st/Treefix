# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/sparse_to_dense_op_test.py
with self.session(), self.test_scope():
    with self.assertRaisesOpError("default_value should be a scalar"):
        _SparseToDense([1, 3], [5], [1, 2], [0])
