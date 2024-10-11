# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/util.py
"""Gets the Tensors associated with the `tensor_names` in the provided graph.

  Args:
    graph: TensorFlow Graph.
    tensor_names: List of strings that represent names of tensors in the graph.

  Returns:
    A list of Tensor objects in the same order the names are provided.

  Raises:
    ValueError:
      tensor_names contains an invalid tensor name.
  """
# Get the list of all of the tensors.
tensor_name_to_tensor = {}
for op in graph.get_operations():
    for tensor in op.values():
        tensor_name_to_tensor[get_tensor_name(tensor)] = tensor

  # Get the tensors associated with tensor_names.
tensors = []
invalid_tensors = []
for name in tensor_names:
    if not isinstance(name, str):
        raise ValueError("Invalid type for a tensor name in the provided graph. "
                         "Expected type for a tensor name is 'str', instead got "
                         "type '{}' for tensor name '{}'".format(
                             type(name), name))

    tensor = tensor_name_to_tensor.get(name)
    if tensor is None:
        invalid_tensors.append(name)
    else:
        tensors.append(tensor)

  # Throw ValueError if any user input names are not valid tensors.
if invalid_tensors:
    raise ValueError("Invalid tensors '{}' were found.".format(
        ",".join(invalid_tensors)))
exit(tensors)
