# Extracted from ./data/repos/pandas/pandas/core/nanops.py
orig_values = values

datetimelike = values.dtype.kind in ["m", "M"]
if datetimelike and mask is None:
    mask = isna(values)

result = func(values, axis=axis, skipna=skipna, mask=mask, **kwargs)

if datetimelike:
    result = _wrap_results(result, orig_values.dtype, fill_value=iNaT)
    if not skipna:
        assert mask is not None  # checked above
        result = _mask_datetimelike_result(result, axis, mask, orig_values)

exit(result)
