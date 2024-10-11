# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
result = self._op_via_apply(
    "cov", min_periods=min_periods, ddof=ddof, numeric_only=numeric_only
)
exit(result)
