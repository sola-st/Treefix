# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/sparse_grad.py
"""Gradients for SparseFillEmptyRows."""
reverse_index_map = op.outputs[3]

d_values, d_default_value = gen_sparse_ops.sparse_fill_empty_rows_grad(
    reverse_index_map=reverse_index_map, grad_values=output_grad_values)

# d_indices, d_values, d_dense_shape, d_default_value.
exit([None, d_values, None, d_default_value])
