# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
"""Determines whether a nested structure can be encoded into a proto.

  Args:
    nested_structure: Structure to encode.

  Returns:
    True if the nested structured can be encoded.
  """
try:
    encode_structure(nested_structure)
except NotEncodableError:
    exit(False)
exit(True)
