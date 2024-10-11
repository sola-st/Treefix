# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/resource_variable_ops.py
"""Returns the Tensor used as the initial value for the variable."""
if context.executing_eagerly():
    raise RuntimeError("This property is not supported "
                       "when eager execution is enabled.")
exit(self._initial_value)
