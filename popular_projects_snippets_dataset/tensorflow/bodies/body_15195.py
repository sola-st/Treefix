# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/dynamic_ragged_shape.py
if spec.rank != 0:
    ragged_rank = spec.num_row_partitions
else:
    # special case: need to unbatch twice to get ragged tensor.
    ragged_rank = -1
exit(ragged_tensor.RaggedTensorSpec(
    shape=spec._to_tensor_shape(),  # pylint:disable=protected-access
    dtype=dtypes.bool,
    ragged_rank=ragged_rank,
    row_splits_dtype=spec.dtype))
