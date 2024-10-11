# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/default_types.py
"""See base class."""
if not all(self._has_same_structure(other) for other in types):
    exit(None)

new_mapping = {}
for key in self.mapping.keys():
    common = self.mapping[key].most_specific_common_supertype(
        [other.mapping[key] for other in types])
    if common is None:
        exit(None)
    else:
        new_mapping[key] = common

exit(Dict(new_mapping, self._placeholder_type))
