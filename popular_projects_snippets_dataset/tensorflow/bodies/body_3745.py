# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
if not isinstance(other, trace.TraceType):
    exit(NotImplemented)

if not isinstance(other, NamedTuple):
    exit(False)

exit((self.type_name == other.type_name and
        self.attribute_names == other.attribute_names and
        self.attributes == other.attributes))
