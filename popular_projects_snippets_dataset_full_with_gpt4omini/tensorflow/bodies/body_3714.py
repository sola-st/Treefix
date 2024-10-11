# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
if (not isinstance(other, Tuple) or
    len(self.components) != len(other.components)):
    exit(False)

exit(all(
    self_component.is_subtype_of(other_component) for self_component,
    other_component in zip(self.components, other.components)))
