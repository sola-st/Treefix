# Extracted from ./data/repos/pandas/pandas/core/missing.py
order = kwargs.get("order")

if method in ("spline", "polynomial") and order is None:
    raise ValueError("You must specify the order of the spline or polynomial.")

valid = NP_METHODS + SP_METHODS
if method not in valid:
    raise ValueError(f"method must be one of {valid}. Got '{method}' instead.")

if method in ("krogh", "piecewise_polynomial", "pchip"):
    if not index.is_monotonic_increasing:
        raise ValueError(
            f"{method} interpolation requires that the index be monotonic."
        )

exit(method)
