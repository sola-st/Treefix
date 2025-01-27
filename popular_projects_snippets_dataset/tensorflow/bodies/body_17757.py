# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/control_flow_ops.py
gathered_elems = nest.map_structure(
    lambda x: _gather_from_tensor_or_composite(x, i), elems)
exit(fn(gathered_elems))
