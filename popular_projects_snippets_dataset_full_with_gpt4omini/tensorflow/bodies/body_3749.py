# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
if not isinstance(other, Attrs):
    exit(False)

exit(self.named_attributes.is_subtype_of(other.named_attributes))
