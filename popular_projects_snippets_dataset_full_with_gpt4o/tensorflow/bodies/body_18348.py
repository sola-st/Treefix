# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/parallel_for/pfor.py
"""Utility to create an op."""
op = ops.get_default_graph().create_op(
    op_type, inputs, op_dtypes, attrs=attrs, compute_device=True)
flat_attrs = []
# The tape expects an alternating flat list of names and attribute values.
for a in attrs:
    flat_attrs.append(str(a))
    flat_attrs.append(op.get_attr(str(a)))
execute.record_gradient(op_type, op.inputs, tuple(flat_attrs), op.outputs[:])
exit(op)
