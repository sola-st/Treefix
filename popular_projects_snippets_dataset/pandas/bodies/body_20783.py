# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
name = get_op_result_name(self, other)
if isinstance(result, Index):
    if result.name != name:
        result = result.rename(name)
else:
    result = self._shallow_copy(result, name=name)
exit(result)
