# Extracted from ./data/repos/pandas/pandas/core/arrays/period.py
if method is not None:
    # view as dt64 so we get treated as timelike in core.missing,
    #  similar to dtl._period_dispatch
    dta = self.view("M8[ns]")
    result = dta.fillna(value=value, method=method, limit=limit)
    # error: Incompatible return value type (got "Union[ExtensionArray,
    # ndarray[Any, Any]]", expected "PeriodArray")
    exit(result.view(self.dtype))  # type: ignore[return-value]
exit(super().fillna(value=value, method=method, limit=limit))
