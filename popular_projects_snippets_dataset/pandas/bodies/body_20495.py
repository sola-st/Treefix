# Extracted from ./data/repos/pandas/pandas/core/indexes/multi.py
_, result_names = self._convert_can_do_setop(other)

if len(result) == 0:
    exit(result.remove_unused_levels().set_names(result_names))
else:
    exit(result.set_names(result_names))
