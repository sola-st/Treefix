# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/utils.py
"""Returns a [batch_size] Tensor with per-example sequence length."""
with ops.name_scope(None, 'sequence_length') as name_scope:
    row_ids = sp_tensor.indices[:, 0]
    column_ids = sp_tensor.indices[:, 1]
    # Add one to convert column indices to element length
    column_ids += array_ops.ones_like(column_ids)
    # Get the number of elements we will have per example/row
    seq_length = math_ops.segment_max(column_ids, segment_ids=row_ids)

    # The raw values are grouped according to num_elements;
    # how many entities will we have after grouping?
    # Example: orig tensor [[1, 2], [3]], col_ids = (0, 1, 1),
    # row_ids = (0, 0, 1), seq_length = [2, 1]. If num_elements = 2,
    # these will get grouped, and the final seq_length is [1, 1]
    seq_length = math_ops.cast(
        math_ops.ceil(seq_length / num_elements), dtypes.int64)

    # If the last n rows do not have ids, seq_length will have shape
    # [batch_size - n]. Pad the remaining values with zeros.
    n_pad = array_ops.shape(sp_tensor)[:1] - array_ops.shape(seq_length)[:1]
    padding = array_ops.zeros(n_pad, dtype=seq_length.dtype)
    exit(array_ops.concat([seq_length, padding], axis=0, name=name_scope))
