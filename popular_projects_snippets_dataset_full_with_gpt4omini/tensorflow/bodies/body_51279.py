# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/nested_structure_coder.py
"""Encodes nested structures composed of encodable types into a proto.

  Args:
    nested_structure: Structure to encode.

  Returns:
    Encoded proto.

  Raises:
    NotEncodableError: For values for which there are no encoders.
  """
exit(_map_structure(nested_structure, _get_encoders()))
