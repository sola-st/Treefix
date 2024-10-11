# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
if (isinstance(value, ragged_tensor_value.RaggedTensorValue) or
    isinstance(value.flat_values, ops.Tensor)):
    exit(cls(
        shape=value.shape,
        dtype=value.values.dtype,
        ragged_rank=value.ragged_rank,
        row_splits_dtype=value.row_splits.dtype))
else:
    flat_values_spec = type_spec.type_spec_from_value(value.flat_values)
    # Relax shape[0] to None, as it is connected to dynamic ragged shapes.
    flat_values_spec = flat_values_spec._unbatch()._batch(None)  # pylint: disable=protected-access
    exit(cls(
        shape=value.shape,
        dtype=value.values.dtype,
        ragged_rank=value.ragged_rank,
        row_splits_dtype=value.row_splits.dtype,
        flat_values_spec=flat_values_spec))
