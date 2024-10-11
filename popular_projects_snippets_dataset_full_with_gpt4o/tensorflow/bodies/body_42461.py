# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function.py
"""Lifts `old_variable` out of the `FuncGraph` `graph`."""
new_variable = resource_variable_ops.UninitializedVariable(
    shape=old_variable.shape,
    dtype=old_variable.dtype,
    name=old_variable.op.name,
    trainable=old_variable.trainable,
    extra_handle_data=old_variable.handle)
new_variable._initializer_op = old_variable._initializer_op  # pylint: disable=protected-access
graph.add_capture(new_variable.handle, old_variable.handle)
# Now that we've added the new variable to graph.captures,
# graph.capture will use that cached value and do some post-processing
# on the capture like recording it on the tape.
graph.capture(new_variable.handle)
# pylint: disable=protected-access
variable_name = new_variable.name.split(":")[0]
variable_holder._variables_by_name[variable_name] = new_variable
graph._weak_variables.append(weakref.ref(new_variable))
# pylint: enable=protected-access
graph.watch_variable(new_variable)
exit(new_variable)
