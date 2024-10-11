# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function.py
"""Conditionally runs initialization if it's needed."""
condition = True
for v, _ in initializers:
    condition = math_ops.logical_and(
        condition, resource_variable_ops.var_is_initialized_op(
            v.handle))
# We want to call no_variable_creation if possible because it avoids
# recomputing potentially expensive initializers.
exit(control_flow_ops.cond(
    condition,
    lambda: self._no_variable_creation_fn(*inner_args, **inner_kwds),
    functools.partial(
        self._concrete_variable_creation_fn._call_flat,  # pylint: disable=protected-access
        inner_filtered_flat_args,
        captured_inputs=self._concrete_variable_creation_fn
        .captured_inputs)))
