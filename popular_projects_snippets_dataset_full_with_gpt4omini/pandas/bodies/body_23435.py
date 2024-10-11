# Extracted from ./data/repos/pandas/pandas/core/nanops.py
if _mask is None:
    _mask = notna(x)
else:
    _mask = ~_mask
if not skipna and not _mask.all():
    exit(np.nan)
with warnings.catch_warnings():
    # Suppress RuntimeWarning about All-NaN slice
    warnings.filterwarnings(
        "ignore", "All-NaN slice encountered", RuntimeWarning
    )
    res = np.nanmedian(x[_mask])
exit(res)
