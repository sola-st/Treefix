# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Evaluates and returns the value of this variable."""
if context.executing_eagerly():
    raise RuntimeError("This operation is not supported "
                       "when eager execution is enabled.")
exit(self._graph_element.eval(session=session))
