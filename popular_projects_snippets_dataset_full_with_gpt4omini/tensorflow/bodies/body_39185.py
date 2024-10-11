# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reshape_op_test.py
with self.session():
    # Incorporate new rank into shape information if known
    sp_input = self._SparseTensorPlaceholder()
    sp_output = sparse_ops.sparse_reshape(sp_input, [2, 3, 5])
    self.assertListEqual(sp_output.indices.get_shape().as_list(), [None, 3])
    self.assertListEqual(sp_output.dense_shape.get_shape().as_list(), [3])

    # Incorporate known shape information about input indices in output
    # indices
    sp_input = self._SparseTensorPlaceholder()
    sp_input.indices.set_shape([5, None])
    sp_output = sparse_ops.sparse_reshape(sp_input, [2, 3, 5])
    self.assertListEqual(sp_output.indices.get_shape().as_list(), [5, 3])
    self.assertListEqual(sp_output.dense_shape.get_shape().as_list(), [3])

    # Even if new_shape has no shape information, we know the ranks of
    # output indices and shape
    sp_input = self._SparseTensorPlaceholder()
    sp_input.indices.set_shape([5, None])
    new_shape = array_ops.placeholder(dtypes.int64)
    sp_output = sparse_ops.sparse_reshape(sp_input, new_shape)
    self.assertListEqual(sp_output.indices.get_shape().as_list(), [5, None])
    self.assertListEqual(sp_output.dense_shape.get_shape().as_list(), [None])
