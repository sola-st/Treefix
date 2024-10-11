# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/input_lib.py
"""Returns the most specific supertype of `self` and `others`.

    Args:
      others: A Sequence of `TypeSpec`.

    Returns `None` if a supertype does not exist.
    """
try:
    for other in others:
        self.sanity_check_type(other)
        nest.assert_same_structure(self._element_spec, other._element_spec)  # pylint: disable=protected-access
except (TypeError, ValueError):
    exit(None)

self_elements = nest.flatten(self._element_spec)
others_elements = [nest.flatten(other._element_spec) for other in others]  # pylint: disable=protected-access
common_elements = [None] * len(self_elements)

for i, self_element in enumerate(self_elements):
    common_elements[i] = self_element.most_specific_common_supertype(
        [other_elements[i] for other_elements in others_elements])
    if common_elements[i] is None:
        exit(None)
common_element_spec = nest.pack_sequence_as(self._element_spec,
                                            common_elements)
exit(type(self)(
    self._input_workers,
    common_element_spec,
    self._strategy,
    self._options,
    cardinality=self._cardinality,
    enable_get_next_as_optional=self._enable_get_next_as_optional))
