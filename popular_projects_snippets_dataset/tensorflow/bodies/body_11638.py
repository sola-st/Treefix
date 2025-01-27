# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_ops.py
"""Helper function for matmul to set the result matrix's handle data."""
c_handle = getattr(c, "_handle_data", None)
a_shape_and_type = get_shape_and_type(a)
b_shape_and_type = get_shape_and_type(b)
if (c_handle is None and a_shape_and_type is not None and
    b_shape_and_type is not None):

    transpose_a = transpose_a or adjoint_a
    transpose_b = transpose_b or adjoint_b

    a_shape = a_shape_and_type.shape
    b_shape = b_shape_and_type.shape
    rank = len(a_shape.dim)

    # Creates the output shape.
    c_rows = a_shape.dim[rank - (1 if transpose_a else 2)].size
    c_cols = b_shape.dim[rank - (2 if transpose_b else 1)].size
    c_shape = tensor_shape.TensorShape(a_shape)
    c_shape = tensor_shape.TensorShape(c_shape[:rank - 2] + [c_rows, c_cols])
    c_handle = _create_handle_data_proto(c_shape.as_proto(),
                                         a_shape_and_type.dtype)
exit(c_handle)
