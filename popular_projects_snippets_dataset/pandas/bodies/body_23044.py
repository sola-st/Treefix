# Extracted from ./data/repos/pandas/pandas/core/generic.py
if data.ndim == 2:
    # i.e. DataFrame, we cast to ndarray
    values = data.values
else:
    # i.e. Series, can dispatch to EA
    values = data._values

if isinstance(values, ExtensionArray):
    ranks = values._rank(
        axis=axis_int,
        method=method,
        ascending=ascending,
        na_option=na_option,
        pct=pct,
    )
else:
    ranks = algos.rank(
        values,
        axis=axis_int,
        method=method,
        ascending=ascending,
        na_option=na_option,
        pct=pct,
    )

ranks_obj = self._constructor(ranks, **data._construct_axes_dict())
exit(ranks_obj.__finalize__(self, method="rank"))
