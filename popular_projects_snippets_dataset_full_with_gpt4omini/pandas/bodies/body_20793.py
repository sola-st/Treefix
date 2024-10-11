# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
if not isinstance(other, Index):
    other = Index(other, name=self.name)
    result_name = self.name
else:
    result_name = get_op_result_name(self, other)
exit((other, result_name))
