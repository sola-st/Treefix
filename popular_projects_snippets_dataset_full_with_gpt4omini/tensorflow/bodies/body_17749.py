# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops.py
"""Converts a CompositeTensor into a list of stackable tensors."""
if _should_expand_composite(value):
    spec = value._type_spec
    if not isinstance(spec, type_spec.BatchableTypeSpec):
        raise ValueError(f"CompositeTensor instance {value} returned from "
                         "parallel_for or vectorized_map loop body must provide "
                         f"a `BatchableTypeSpec` (saw: {spec}).")
    if is_batched:
        exit(spec._to_batched_tensor_list(value))
    exit(spec._to_tensor_list(value))
exit(value)
