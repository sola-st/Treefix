# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla.py
"""Builds a new XLACompileContext.

    Args:
      name: a unique name for the context, used to populate the
        `_xla_compile_id` attribute.
      pivot: a pivot node. Nodes in the XLACompileContext that do not have any
        inputs will have a control dependency on the pivot node. This ensures
        that nodes are correctly included in any enclosing control flow
        contexts.
    """
super(XLACompileContext, self).__init__()
self._name = name
self._name_as_bytes = compat.as_bytes(name)
self._unsupported_ops = []
self._pivot = pivot
