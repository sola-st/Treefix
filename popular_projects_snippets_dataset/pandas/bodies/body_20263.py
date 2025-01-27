# Extracted from ./data/repos/pandas/pandas/core/missing.py
"""
    Apply interpolation and limit_area logic to values along a to-be-specified axis.

    Parameters
    ----------
    values: np.ndarray
        Input array.
    method: str
        Interpolation method. Could be "bfill" or "pad"
    limit: int, optional
        Index limit on interpolation.
    limit_area: str
        Limit area for interpolation. Can be "inside" or "outside"

    Notes
    -----
    Modifies values in-place.
    """

invalid = isna(values)
is_valid = ~invalid

if not invalid.all():
    first = find_valid_index(values, how="first", is_valid=is_valid)
    if first is None:
        first = 0
    last = find_valid_index(values, how="last", is_valid=is_valid)
    if last is None:
        last = len(values)

    interpolate_2d(
        values,
        method=method,
        limit=limit,
    )

    if limit_area == "inside":
        invalid[first : last + 1] = False
    elif limit_area == "outside":
        invalid[:first] = invalid[last + 1 :] = False

    values[invalid] = np.nan
