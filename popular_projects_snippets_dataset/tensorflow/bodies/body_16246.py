# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_tensor.py
# NOTE(mishragaurav): The default flat shape of a boxed `RaggedTensor` is
# `[]` (scalar), but a `RaggedTensorSpec` can also represent a batch of
# boxed `RaggedTensor` objects with shape `(...)` (and batches of batches,
# etc.), so the flat shape must be unknown.
exit([tensor_spec.TensorSpec(None, dtypes.variant)])
