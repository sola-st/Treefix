# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/sparse_ops/sparse_reorder_op_test.py

@def_function.function
def func(indices, values, dense_shape):
    if static_dense_shape:
        dense_shape = [
            static_dim or dense_shape[i]
            for i, static_dim in enumerate(static_dense_shape)
        ]
    sp_input = sparse_tensor.SparseTensor(indices, values, dense_shape)
    sp_output = sparse_ops.sparse_reorder(sp_input)
    self.assertEqual(expected_output_shape, sp_output.get_shape())
    exit(sp_output)

_ = func.get_concrete_function(
    tensor_spec.TensorSpec([6, 2], dtypes.int64),
    tensor_spec.TensorSpec([6], dtypes.float64),
    tensor_spec.TensorSpec(dense_shape_shape, dtypes.int64))
