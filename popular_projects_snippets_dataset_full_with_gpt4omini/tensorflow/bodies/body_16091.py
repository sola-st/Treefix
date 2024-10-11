# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_map_ops.py
if isinstance(t, ragged_tensor.RaggedTensorType):
    # Note: need to adjust ragged_rank by 1, since RaggedTensorSpec gives the
    # type for the mapped `fn` output, but RaggedTensorType gives the type for
    # the result of stacking the mapped `fn` outputs.
    exit(ragged_tensor.RaggedTensorSpec(
        None, t.dtype, t.ragged_rank - 1, t.row_splits_dtype))
else:
    exit(t)
