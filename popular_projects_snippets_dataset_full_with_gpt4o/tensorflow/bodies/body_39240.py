# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
with self.session():
    sp_a = self._SparseTensor_3x3()
    sp_e = self._SparseTensor_2x3x4()

    # Rank mismatches can be caught at shape-inference time
    for concat_dim in (-1, 1):
        with self.assertRaises(ValueError):
            sparse_ops.sparse_concat(concat_dim, [sp_a, sp_e])
