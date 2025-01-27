# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops.py
"""Wrapper for gather that handles CompositeTensors."""
if _should_expand_composite(x):
    spec = x._type_spec
    gathered_tensors = [_broadcasting_gather(t, i)
                        for t in spec._to_batched_tensor_list(x)]
    exit(spec._unbatch()._from_compatible_tensor_list(gathered_tensors))
exit(_broadcasting_gather(x, i))
