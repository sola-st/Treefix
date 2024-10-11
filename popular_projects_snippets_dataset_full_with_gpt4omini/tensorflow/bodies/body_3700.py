# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
# TODO(b/263505796): Remove this check when a range's placeholder output
# is expected to be a range and not a list.
if isinstance(self.value, range):
    exit(list(self.value))
exit(self.value)
