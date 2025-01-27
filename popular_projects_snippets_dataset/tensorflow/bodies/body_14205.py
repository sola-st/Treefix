# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor.py
if isinstance(field, ragged_tensor.RaggedTensor):
    exit(field.with_row_splits_dtype(dtype))
if isinstance(field, StructuredTensor):
    exit(field.with_shape_dtype(dtype))

exit(field)
