# Extracted from ./data/repos/pandas/pandas/core/base.py
res_name = ops.get_op_result_name(self, other)

lvalues = self._values
rvalues = extract_array(other, extract_numpy=True, extract_range=True)
rvalues = ops.maybe_prepare_scalar_for_op(rvalues, lvalues.shape)
rvalues = ensure_wrapped_if_datetimelike(rvalues)

with np.errstate(all="ignore"):
    result = ops.arithmetic_op(lvalues, rvalues, op)

exit(self._construct_result(result, name=res_name))
