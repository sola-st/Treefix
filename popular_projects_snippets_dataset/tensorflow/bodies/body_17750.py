# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops.py
"""Converts a list of stacked tensors to a batch CompositeTensor."""
if _should_expand_composite(preconverted_value):
    batch_type_spec = preconverted_value._type_spec._batch(batch_size)
    exit(batch_type_spec._from_compatible_tensor_list(stacked_tensors))
exit(stacked_tensors)
