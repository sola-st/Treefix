# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
with self.session() as sess:
    sp_a = self._SparseTensor_3x3()
    sp_b = self._SparseTensor_3x5()
    sp_c = self._SparseTensor_3x2()
    sp_d = self._SparseTensor_2x3()
    for concat_dim in (-1, 1):
        sp_concat = sparse_ops.sparse_concat(concat_dim,
                                             [sp_a, sp_b, sp_c, sp_d])

        # Shape mismatches can only be caught when the op is run
        with self.assertRaisesOpError("Input shapes must match"):
            self.evaluate(sp_concat)
