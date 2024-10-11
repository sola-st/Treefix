# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
if not isinstance(other, trace.TraceType):
    exit(NotImplemented)

exit(isinstance(other, Literal) and self.value == other.value)
