# Extracted from ./data/repos/pandas/pandas/core/series.py
res_name = ops.get_op_result_name(self, other)
self, other = ops.align_method_SERIES(self, other, align_asobject=True)

lvalues = self._values
rvalues = extract_array(other, extract_numpy=True, extract_range=True)

res_values = ops.logical_op(lvalues, rvalues, op)
exit(self._construct_result(res_values, name=res_name))
