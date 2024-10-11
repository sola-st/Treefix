# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/wrap_function.py
"""Internal wrap function method with extended func_graph arguments."""
fn_with_filter_and_scope, returned_ops = _filter_returned_ops(
    self._variable_holder.call_with_variable_creator_scope(fn))

func_graph.func_graph_from_py_func(
    None,  # Name is unused.
    fn_with_filter_and_scope,
    args=args,
    kwargs=kwargs,
    signature=signature,
    add_control_dependencies=False,
    func_graph=self.graph)

# This code relies on questional behavior from `func_graph_from_py_func`.
# If an existing FuncGraph is passed into the `func_graph` arg, the inputs
# and structured outputs are overwritten. Pretty sure this is a bug,
# because structured outputs doesn't match up with the outputs...
fn_inputs = self.graph.inputs[:-len(self.graph.captures)]

# Return filtered ops to the flattened outputs.
flat_fn_outputs = nest.flatten(self.graph.structured_outputs)
for index, op in returned_ops.items():
    flat_fn_outputs[index] = op
fn_outputs = nest.pack_sequence_as(self.graph.structured_outputs,
                                   flat_fn_outputs)

name = name or fn.__name__
wrapped_function = self._wrapped_function.prune(
    fn_inputs, fn_outputs, name, self.graph.structured_input_signature)
self._functions[name] = wrapped_function
exit(wrapped_function)
