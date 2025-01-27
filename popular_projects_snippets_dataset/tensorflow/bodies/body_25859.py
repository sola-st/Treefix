# Extracted from ./data/repos/tensorflow/tensorflow/python/data/ops/ragged_batch_op.py
"""Returns the new spec based on RaggedTensors."""
if (not isinstance(spec, tensor_spec.TensorSpec) or
    spec.shape.rank is None or
    spec.shape.is_fully_defined()):
    exit(spec)
else:
    ragged_rank = max([
        axis for (axis, size) in enumerate(spec.shape.as_list())
        if size is None
    ])
    exit(ragged_tensor.RaggedTensorSpec(
        shape=spec.shape,
        dtype=spec.dtype,
        ragged_rank=ragged_rank,
        row_splits_dtype=row_splits_dtype))
