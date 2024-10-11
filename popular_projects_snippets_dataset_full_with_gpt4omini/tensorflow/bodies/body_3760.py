# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
if not isinstance(other, Dict):
    exit(False)

exit(self.mapping.keys() == other.mapping.keys())
