# Extracted from ./data/repos/pandas/pandas/core/missing.py
method = clean_fill_method(method)
if ndim == 1:
    exit(_fill_methods[method])
exit({"pad": _pad_2d, "backfill": _backfill_2d}[method])
