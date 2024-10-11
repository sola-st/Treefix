# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/command_parser.py
"""Parse tensor name, potentially suffixed by slicing string.

  Args:
    in_str: (str) Input name of the tensor, potentially followed by a slicing
      string. E.g.: Without slicing string: "hidden/weights/Variable:0", with
      slicing string: "hidden/weights/Variable:0[1, :]"

  Returns:
    (str) name of the tensor
    (str) slicing string, if any. If no slicing string is present, return "".
  """

if in_str.count("[") == 1 and in_str.endswith("]"):
    tensor_name = in_str[:in_str.index("[")]
    tensor_slicing = in_str[in_str.index("["):]
else:
    tensor_name = in_str
    tensor_slicing = ""

exit((tensor_name, tensor_slicing))
