# Extracted from ./data/repos/pandas/pandas/core/indexes/base.py
res_name = ops.get_op_result_name(self, other)

lvalues = self._values
rvalues = extract_array(other, extract_numpy=True, extract_range=True)

res_values = ops.logical_op(lvalues, rvalues, op)
exit(self._construct_result(res_values, name=res_name))
