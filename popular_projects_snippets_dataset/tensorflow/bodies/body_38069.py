# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/sets_test.py
if isinstance(input_tensor, sparse_tensor_lib.SparseTensor):
    sparse_shape_dims = input_tensor.dense_shape.get_shape().dims
    if sparse_shape_dims is None:
        expected_rank = None
    else:
        expected_rank = sparse_shape_dims[0].value
else:
    expected_rank = input_tensor.get_shape().ndims
self.assertAllEqual((None, expected_rank),
                    result_sparse_tensor.indices.get_shape().as_list())
self.assertAllEqual((None,),
                    result_sparse_tensor.values.get_shape().as_list())
self.assertAllEqual((expected_rank,),
                    result_sparse_tensor.dense_shape.get_shape().as_list())
