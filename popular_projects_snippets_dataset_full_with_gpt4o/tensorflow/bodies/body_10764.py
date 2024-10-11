# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
"""Creates a `CondContext`.

    Args:
      pred: The `boolean` tensor for the conditional predicate.
      pivot: The predicate tensor in this branch.
      branch: 0 or 1 representing this branch.
      name: Name of the `CondContext` python object.
      context_def: Optional `ContextDef` protocol buffer to initialize the
        `CondContext` object from.
      import_scope: Optional `string`. Name scope to add. Only used when
        initialing from protocol buffer.
    """
self._name = ops.get_default_graph().unique_name(name)

if context_def:
    self._init_from_proto(context_def, import_scope=import_scope)
else:
    # Initializes the default fields.
    ControlFlowContext.__init__(self)
    self._pred = pred  # The boolean tensor for the cond predicate
    self._pivot = pivot  # The predicate tensor in this branch
    self._branch = branch  # 0 or 1 representing this branch

    # Values considered to have been already seen in this context. pred is not
    # included in this context.
    self._values.add(pred.name)
    self._external_values[pred.name] = pred
    self._values.add(pivot.name)
    pivot.op._set_control_flow_context(self)  # pylint: disable=protected-access
