# Extracted from ./data/repos/pandas/pandas/core/missing.py
if needs_i8_conversion(values.dtype):
    if mask is None:
        # This needs to occur before casting to int64
        mask = isna(values)

    result, mask = func(values.view("i8"), limit=limit, mask=mask)
    exit((result.view(values.dtype), mask))

exit(func(values, limit=limit, mask=mask))
