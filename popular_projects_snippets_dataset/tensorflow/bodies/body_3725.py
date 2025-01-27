# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
if not isinstance(other, List):
    exit(False)

exit(self.components_tuple.is_subtype_of(other.components_tuple))
