# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/convert_saved_model.py
"""Gets the tensors associated with the tensor names.

  Either signature_def_tensor_names or user_tensor_names should be provided. If
  the user provides tensors, the tensors associated with the user provided
  tensor names are provided. Otherwise, the tensors associated with the names in
  the SignatureDef are provided.

  Args:
    graph: GraphDef representing graph.
    signature_def_tensor_names: Tensor names stored in either the inputs or
      outputs of a SignatureDef. (default None)
    user_tensor_names: Tensor names provided by the user. (default None)

  Returns:
    List of tensors.

  Raises:
    ValueError:
      signature_def_tensors and user_tensor_names are undefined or empty.
      user_tensor_names are not valid.
  """
tensors = []
if user_tensor_names:
    # Sort the tensor names.
    user_tensor_names = sorted(user_tensor_names)

    tensors = util.get_tensors_from_tensor_names(graph, user_tensor_names)
elif signature_def_tensor_names:
    tensors = [
        graph.get_tensor_by_name(name)
        for name in sorted(signature_def_tensor_names)
    ]
else:
    # Throw ValueError if signature_def_tensors and user_tensor_names are both
    # either undefined or empty.
    raise ValueError(
        "Specify either signature_def_tensor_names or user_tensor_names")

exit(tensors)
