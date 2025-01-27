# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/linalg/sparse/csr_sparse_matrix_ops_test.py
if not self._gpu_available:
    exit()

a_indices = np.array([[0, 0], [2, 3]])
a_values = np.asarray([1.0, 5.0], dtype=np.float32)
a_dense_shape = np.asarray([5, 6], dtype=np.int64)
a_sparse_mat = sparse.coo_matrix(
    (a_values, (a_indices[:, 0], a_indices[:, 1])), shape=a_dense_shape)
a_csr_mat = a_sparse_mat.tocsr()
a_col_inds = a_csr_mat.indices
a_row_ptrs = a_csr_mat.indptr

# Format of SparseMatrix:
#  type_name == "tensorflow::CSRSparseMatrix"
#  metadata == b (validated)
#  tensors == [dense_shape, row_ptrs, col_indices, values]
dense_shape_proto = tensor_util.make_tensor_proto(a_dense_shape)
row_ptrs_proto = tensor_util.make_tensor_proto(a_row_ptrs)
col_inds_proto = tensor_util.make_tensor_proto(a_col_inds)
values_proto = tensor_util.make_tensor_proto(a_values)
variant_tensor_data = tensor_pb2.VariantTensorDataProto(
    type_name="tensorflow::CSRSparseMatrix",
    metadata=np.asarray(True).tobytes(),
    tensors=[
        dense_shape_proto, row_ptrs_proto, col_inds_proto, values_proto
    ])
tensor_proto = tensor_pb2.TensorProto(
    dtype=dtypes.variant.as_datatype_enum,
    tensor_shape=tensor_shape.TensorShape([]).as_proto())
tensor_proto.variant_val.extend([variant_tensor_data])
a_sm = constant_op.constant(tensor_proto)
a_rt = sparse_csr_matrix_ops.csr_sparse_matrix_to_dense(
    a_sm, type=dtypes.float32)
self.evaluate(a_rt)
