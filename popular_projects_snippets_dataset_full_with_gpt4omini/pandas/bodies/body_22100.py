# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
result = self._op_via_apply(
    "skew",
    axis=axis,
    skipna=skipna,
    numeric_only=numeric_only,
    **kwargs,
)
exit(result)
