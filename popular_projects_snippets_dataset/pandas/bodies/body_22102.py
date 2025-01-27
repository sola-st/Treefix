# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
result = self._op_via_apply(
    "corr", method=method, min_periods=min_periods, numeric_only=numeric_only
)
exit(result)
