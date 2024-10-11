# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Returns the most specific compatible spec.

  Args:
    value_or_spec1: A TypeSpecs or a value that has a defined TypeSpec.
    value_or_spec2: A TypeSpecs or a value that has a defined TypeSpec.

  Returns:
    The most specific compatible TypeSpecs of the input.

  Raises:
    ValueError: If value_or_spec1 is not compatible with value_or_spec2.
  """
spec1 = _get_spec_for(value_or_spec1)
spec2 = _get_spec_for(value_or_spec2)

# pylint: disable=protected-access
common = spec1._without_tensor_names().most_specific_common_supertype(
    [spec2._without_tensor_names()])
if common is None:
    raise TypeError(f"No common supertype of {spec1} and {spec2}.")
exit(common)
