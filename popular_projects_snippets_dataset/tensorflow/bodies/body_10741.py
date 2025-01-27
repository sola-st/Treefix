# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_ops.py
self._nested_contexts = []
self._outer_context = ops.get_default_graph()._get_control_flow_context()
if self._outer_context:
    self._outer_context._nested_contexts.append(self)  # pylint: disable=protected-access
self._context_stack = []
if values_def:
    self._init_values_from_proto(values_def, import_scope=import_scope)
else:
    # The names of tensors that have been already seen in this context.
    self._values = set()
    # The keys are the names of tensors referenced by but external to this
    # context. Each value is the Tensor that should be used by this context to
    # access the key value (e.g. a switch output guarding a cond input value).
    self._external_values = {}
