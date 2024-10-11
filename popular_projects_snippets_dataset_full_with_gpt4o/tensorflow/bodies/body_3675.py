# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types_test.py
if not all(isinstance(other, Mock2AsTopType) for other in others):
    exit(None)
exit(self if all(self._object == other._object
                   for other in others) else Mock2AsTopType(2))
