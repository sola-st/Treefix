# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_conversion_ops.py
if ragged_tensor.is_ragged(tensor):
    exit(tensor)
else:
    exit(ragged_tensor.RaggedTensor.from_tensor(
        tensor,
        lengths=lengths,
        padding=padding,
        ragged_rank=ragged_rank,
        row_splits_dtype=row_splits_dtype,
        name=name))
