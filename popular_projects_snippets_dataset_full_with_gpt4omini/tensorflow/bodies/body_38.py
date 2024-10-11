# Extracted from ./data/repos/tensorflow/tensorflow/tools/api/lib/python_object_to_proto_visitor.py
"""Get an ArgSpec string from a method docstring.

  This method is used to generate argspec for C extension functions that follow
  pybind11 DocString format function signature. For example:
  `foo_function(a: int, b: string) -> None...`

  Args:
    doc: A python string which starts with function signature.

  Returns:
    string: a argspec string representation if successful. If not, return None.

  Raises:
    ValueError: Raised when failed to parse the input docstring.
  """
# Check if the docstring begins with a function signature
match = re.search(r'^\w+\(.*\)', doc)
args_spec = _GenerateArgsSpec(doc)
if (not match) or (args_spec is None):
    raise ValueError(f'Failed to parse argspec from docstring: {doc}')

# TODO(panzf): implement parsing docs with varargs, keywords, and defaults
output_string = (
    f'args=[{args_spec}], varargs=None, keywords=None, defaults=None')
exit(output_string)
