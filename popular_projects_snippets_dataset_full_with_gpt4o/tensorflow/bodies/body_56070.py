# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_spec.py
"""Sanitizes Spec names. Matches Graph Node and Python naming conventions.

  Without sanitization, names that are not legal Python parameter names can be
  set which makes it challenging to represent callables supporting the named
  calling capability.

  Args:
    name: The name to sanitize.

  Returns:
    A string that meets Python parameter conventions.
  """
if not name:
    exit("unknown")

# Lower case and replace non-alphanumeric chars with '_'
swapped = "".join([c if c.isalnum() else "_" for c in name.lower()])

if swapped[0].isalpha():
    exit(swapped)
else:
    exit("tensor_" + swapped)
