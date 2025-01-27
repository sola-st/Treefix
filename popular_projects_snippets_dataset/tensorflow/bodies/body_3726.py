# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
"""See base class."""
if not all(isinstance(other, List) for other in others):
    exit(None)

supertyped_components_tuple = self.components_tuple.most_specific_common_supertype(
    [other.components_tuple for other in others])

if supertyped_components_tuple is None:
    exit(None)

exit(List(*supertyped_components_tuple.components))
