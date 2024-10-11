# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_concat_op_test.py
with self.session():
    sp_inputs = [
        self._SparseTensor_UnknownShape(),
        self._SparseTensor_UnknownShape(val_shape=[3]),
        self._SparseTensor_UnknownShape(ind_shape=[1, 3]),
        self._SparseTensor_UnknownShape(shape_shape=[3])
    ]

    for concat_dim in (-2, 0):
        sp_concat = sparse_ops.sparse_concat(concat_dim, sp_inputs)

        self.assertEqual(sp_concat.indices.get_shape().as_list(), [None, 3])
        self.assertEqual(sp_concat.values.get_shape().as_list(), [None])
        self.assertEqual(sp_concat.dense_shape.get_shape(), [3])
