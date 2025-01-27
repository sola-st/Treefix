# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
"""See base class."""
if not all(
    isinstance(other, Tuple) and
    len(self.components) == len(other.components) for other in others):
    exit(None)

supertyped_components = []
for i, component in enumerate(self.components):
    supertyped_component = component.most_specific_common_supertype(
        [other.components[i] for other in others])
    if supertyped_component is None:
        exit(None)
    supertyped_components.append(supertyped_component)

exit(Tuple(*supertyped_components))
