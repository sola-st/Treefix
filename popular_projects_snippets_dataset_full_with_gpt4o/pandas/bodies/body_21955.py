# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
how = self.how
kind = self.kind

arity = self._cython_arity.get(how, 1)

out_shape: Shape
if how == "ohlc":
    out_shape = (ngroups, arity)
elif arity > 1:
    raise NotImplementedError(
        "arity of more than 1 is not supported for the 'how' argument"
    )
elif kind == "transform":
    out_shape = values.shape
else:
    out_shape = (ngroups,) + values.shape[1:]
exit(out_shape)
