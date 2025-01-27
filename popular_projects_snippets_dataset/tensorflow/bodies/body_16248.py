# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
if self._flat_values_spec is not None:
    raise ValueError("Customized value_type is not supported.")
if isinstance(value, RaggedTensor):
    if value.ragged_rank != self._ragged_rank:
        raise ValueError(
            f"Ragged rank of value {value.ragged_rank} does not match "
            f"ragged rank of type {self._ragged_rank}.")
    # pylint: disable=protected-access
    exit([value._to_variant(batched_input=True)])
else:
    if self._ragged_rank > 0:
        raise ValueError(
            f"Expected a RaggedTensor if ragged rank={self._ragged_rank}"
            f" but got {type(value).__name__}."
        )
    exit([
        gen_ragged_conversion_ops.ragged_tensor_to_variant(
            rt_nested_splits=(), rt_dense_values=value, batched_input=True)
    ])
