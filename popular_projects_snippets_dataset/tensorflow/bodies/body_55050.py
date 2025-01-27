# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""A custom variable getter."""
# Here, we switch the default graph to the outer graph and ask the
# variable scope in which the function is defined to give us the
# variable. The variable is stashed in extra_vars and returned to
# the caller.
#
# We capture these variables so that the variable definition is
# hoisted upward to the outer most graph.
with self._outer_graph.as_default():
    # pylint: disable=protected-access
    var = self._vscope.get_variable(
        vs._get_default_variable_store(),
        name,
        shape=shape,
        dtype=dtype,
        initializer=initializer,
        reuse=reuse,
        trainable=trainable,
        collections=collections,
        use_resource=use_resource)
    self.extra_vars.append(var)
    if (isinstance(var, resource_variable_ops.BaseResourceVariable) and
        self._capture_resource_var_by_value):
        # For resource-based variables read the variable outside the function
        # and pass in the value. This ensures that the function is pure and
        # differentiable. TODO(apassos) this may have performance problems if
        # the function will only do embedding lookups on the variable.
        exit(var.value())
    exit(var)
