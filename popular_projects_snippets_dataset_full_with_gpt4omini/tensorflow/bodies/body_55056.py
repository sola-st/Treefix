# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
# pylint: disable=protected-access
op_def = graph_to_function_def._get_op_def(op)
if op._is_stateful and op not in self._allowlisted_stateful_ops:
    raise ValueError(f"Cannot capture a stateful node (name:{op.name}, "
                     f"type:{op.type}) by value.")
elif op.type in ("Placeholder", "PlaceholderV2"):
    raise ValueError(f"Cannot capture a placeholder (name:{op.name}, "
                     f"type:{op.type}) by value.")
# pylint: enable=protected-access

captured_inputs = [self._add_tensor_and_parents(x) for x in op.inputs]

captured_op = self._create_op_internal(
    op.type,
    captured_inputs, [o.dtype for o in op.outputs],
    name=op.name,
    attrs=op.node_def.attr,
    op_def=op_def)

for t, captured_t in zip(op.outputs, captured_op.outputs):
    self._captured[t.ref()] = captured_t

exit(captured_op)
