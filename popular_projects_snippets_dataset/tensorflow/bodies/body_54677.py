# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""Constructs a concrete function from the `output_graph_def`.

  Args:
    func: ConcreteFunction
    output_graph_def: GraphDef proto.
    converted_input_indices: Set of integers of input indices that were
      converted to constants.

  Returns:
    ConcreteFunction.
  """
# Create a ConcreteFunction from the new GraphDef.
input_tensors = func.graph.internal_captures
converted_inputs = object_identity.ObjectIdentitySet(
    [input_tensors[index] for index in converted_input_indices])
not_converted_inputs = [
    tensor for tensor in func.inputs if tensor not in converted_inputs
]
not_converted_inputs_map = {
    tensor.name: tensor for tensor in not_converted_inputs
}

new_input_names = [tensor.name for tensor in not_converted_inputs]
new_output_names = [tensor.name for tensor in func.outputs]

# Remove old functions to use updated functions from graph def.
for f in output_graph_def.library.function:
    if context.context().has_function(f.signature.name):
        context.context().remove_function(f.signature.name)

new_func = wrap_function.function_from_graph_def(output_graph_def,
                                                 new_input_names,
                                                 new_output_names)

# Manually propagate shape for input tensors where the shape is not correctly
# propagated. Scalars shapes are lost when wrapping the function.
for input_tensor in new_func.inputs:
    input_tensor.set_shape(not_converted_inputs_map[input_tensor.name].shape)
exit(new_func)
