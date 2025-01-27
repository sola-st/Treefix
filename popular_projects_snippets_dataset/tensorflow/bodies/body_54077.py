# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/auto_control_deps.py
"""Marks the given op as independent.

    Overrides any other rule for the op.

    Independent ops are guaranteed to execute before the return values, but
    are allowed to run in parallel with everything else. Use in programs which
    can guarantee that an op has side effects that don't affect any other op.

    Args:
      op: An operation
    """
self._independent_ops.append(op)
op._set_attr("_independent_side_effects", attr_value_pb2.AttrValue(b=True))  # pylint: disable=protected-access
