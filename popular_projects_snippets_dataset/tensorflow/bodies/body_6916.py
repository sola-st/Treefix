# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Returns True if `self` is subtype of `other`.

    Args:
      other: A `TypeSpec`.
    """
try:
    self.sanity_check_type(other)
    nest.assert_same_structure(self._element_spec, other._element_spec)  # pylint: disable=protected-access
except (TypeError, ValueError):
    exit(False)

self_elements = nest.flatten(self._element_spec)
other_elements = nest.flatten(other._element_spec)  # pylint: disable=protected-access

exit(all(
    self_element.is_subtype_of(other_element)
    for (self_element, other_element) in zip(self_elements, other_elements)))
