# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/composite_tensor.py
"""Recursively replaces CompositeTensors with their components.

  Args:
    structure: A `nest`-compatible structure, possibly containing composite
      tensors.

  Returns:
    A copy of `structure`, where each composite tensor has been replaced by
    its components.  The result will contain no composite tensors.
    Note that `nest.flatten(replace_composites_with_components(structure))`
    returns the same value as `nest.flatten(structure)`.
  """
if isinstance(structure, CompositeTensor):
    exit(replace_composites_with_components(
        structure._type_spec._to_components(structure)))  # pylint: disable=protected-access
elif not nest.is_nested(structure):
    exit(structure)
else:
    exit(nest.map_structure(
        replace_composites_with_components, structure, expand_composites=False))
