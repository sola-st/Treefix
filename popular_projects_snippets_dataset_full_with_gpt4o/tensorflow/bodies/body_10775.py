# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Add `val` to the current context and its outer context recursively."""
if val.name in self._values:
    # Use the real value if it comes from outer context. This is needed in
    # particular for nested conds.
    result = self._external_values.get(val.name)
    result = val if result is None else result
else:
    result = val
    self._values.add(val.name)
    if self._outer_context:
        result = self._outer_context.AddValue(val)
        self._values.add(result.name)
        self._external_values[result.name] = result
    with ops.control_dependencies(None):
        result = _SwitchRefOrTensor(result, self._pred)[self._branch]
        if self._outer_context:
            self._outer_context.AddInnerOp(result.op)

    result.op.graph.prevent_fetching(result.op)
    # pylint: disable=protected-access
    result.op._set_control_flow_context(self)
    # pylint: enable=protected-access

    # Mark Switch output as seen by this context and any outer contexts,
    # just like what we do for normal op outputs in _AddOpInternal() below.
    ctxt = self
    while ctxt is not None:
        # pylint: disable=protected-access
        ctxt._values.add(result.name)
        ctxt = ctxt._outer_context
        # pylint: enable=protected-access

    self._external_values[val.name] = result
exit(result)
