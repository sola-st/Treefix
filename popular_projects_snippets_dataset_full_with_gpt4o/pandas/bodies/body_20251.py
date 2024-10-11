# Extracted from ./data/repos/pandas/pandas/core/missing.py
# asfreq is compat for resampling
if method in [None, "asfreq"]:
    exit(None)

if isinstance(method, str):
    method = method.lower()
    if method == "ffill":
        method = "pad"
    elif method == "bfill":
        method = "backfill"

valid_methods = ["pad", "backfill"]
expecting = "pad (ffill) or backfill (bfill)"
if allow_nearest:
    valid_methods.append("nearest")
    expecting = "pad (ffill), backfill (bfill) or nearest"
if method not in valid_methods:
    raise ValueError(f"Invalid fill method. Expecting {expecting}. Got {method}")
exit(method)
