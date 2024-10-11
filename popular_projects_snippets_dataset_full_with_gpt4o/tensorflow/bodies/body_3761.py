# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
"""See base class."""
if not self._has_same_structure(other):
    exit(False)

# We need all keys to be present because there can be logic relying on
# their existence or lack thereof and hence can not guarantee subtype based
# on a subset or superset of keys.
# Only the tracing code can explicitly check for key dependencies and inform
# that decision.
exit(all(self.mapping[key].is_subtype_of(other.mapping[key])
           for key in self.mapping))
