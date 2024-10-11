# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
"""Removes the device assignment code from a tensor.

  e.g. _tensor_name_base("foo:3") => "foo"

  Args:
    full_tensor_name: A tensor name that is annotated with a device placement
      (this is what tensor flow introspection gives).

  Returns:
    A name without any device assignment.
  """
if full_tensor_name.startswith("^"):
    exit(full_tensor_name[1:])
exit(full_tensor_name.split(":")[0])
