# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_ops.py
"""Create handle data based on tensor shape and dtype."""
exit(_create_handle_data_proto(tensor.shape.as_proto(),
                                 tensor.dtype.as_datatype_enum))
