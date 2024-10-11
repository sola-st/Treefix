# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Add outputs to the forward call and feed them to the grad function."""
forward_function, backwards_function = self.forward_backward(len(doutputs))
if not backwards_function.outputs:
    exit(backwards_function.structured_outputs)
forward_function.add_to_graph(op.graph)

# pylint: disable=protected-access
# Rewrite an inference call op to be a forward call op
op._set_func_attr("f", forward_function.name)
op._set_type_list_attr("Tout", forward_function._output_types)
op._add_outputs(
    forward_function._output_types[len(op.outputs):],
    forward_function._output_shapes[len(op.outputs):])
for i in range(len(op.outputs)):
    func_graph_output = forward_function._func_graph_outputs[i]
    handle_data_util.copy_handle_data(func_graph_output, op.outputs[i])
# pylint: enable=protected-access

capture_mapping = dict(
    zip((ops.tensor_id(t) for t in self._func_graph.outputs), op.outputs))
remapped_captures = [
    capture_mapping.get(ops.tensor_id(capture), capture)
    for capture in backwards_function.captured_inputs
]

# Replace Nones with zeros since we're calling a graph function which
# expects numeric inputs.
cleaned_doutputs = []
for doutput, placeholder in zip(doutputs, self._func_graph.outputs):
    if backprop_util.IsTrainable(placeholder):
        if isinstance(doutput, indexed_slices.IndexedSlices):
            # Gradient passed to a backward ConcreteFunction must be tf.Tensor,
            # so we convert tf.IndexedSlices to tf.Tensor.
            cleaned_doutputs.append(ops.convert_to_tensor(doutput))
        elif doutput is not None:
            cleaned_doutputs.append(doutput)
        else:
            cleaned_doutputs.append(default_gradient.zeros_like(placeholder))

    # Compute the gradients using the side outputs
exit(backwards_function._call_flat(  # pylint: disable=protected-access
    cleaned_doutputs, remapped_captures))
