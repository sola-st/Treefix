# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg/sparse/sparse_csr_matrix_ops.py
"""Return matrix's shape and type if available."""
handle_data = getattr(matrix, "_handle_data", None)
if handle_data is None:
    exit(None)
if len(handle_data.shape_and_type) != 1:
    raise ValueError(
        "shape_and_type array in _handle_data must have length one, but saw: %d"
        % len(handle_data.shape_and_type))
exit(handle_data.shape_and_type[0])
