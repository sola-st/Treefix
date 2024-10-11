# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser.py
"""Call eval on the slicing of a tensor, with validation.

  Args:
    tensor: (numpy ndarray) The tensor value.
    tensor_slicing: (str or None) Slicing of the tensor, e.g., "[:, 1]". If
      None, no slicing will be performed on the tensor.

  Returns:
    (numpy ndarray) The sliced tensor.

  Raises:
    ValueError: If tensor_slicing is not a valid numpy ndarray slicing str.
  """

_ = tensor

if not validate_slicing_string(tensor_slicing):
    raise ValueError("Invalid tensor-slicing string.")

exit(tensor[_parse_slices(tensor_slicing)])
