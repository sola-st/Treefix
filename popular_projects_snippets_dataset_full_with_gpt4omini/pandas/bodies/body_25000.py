# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""
    Outputs rounded and formatted percentiles.

    Parameters
    ----------
    percentiles : list-like, containing floats from interval [0,1]

    Returns
    -------
    formatted : list of strings

    Notes
    -----
    Rounding precision is chosen so that: (1) if any two elements of
    ``percentiles`` differ, they remain different after rounding
    (2) no entry is *rounded* to 0% or 100%.
    Any non-integer is always rounded to at least 1 decimal place.

    Examples
    --------
    Keeps all entries different after rounding:

    >>> format_percentiles([0.01999, 0.02001, 0.5, 0.666666, 0.9999])
    ['1.999%', '2.001%', '50%', '66.667%', '99.99%']

    No element is rounded to 0% or 100% (unless already equal to it).
    Duplicates are allowed:

    >>> format_percentiles([0, 0.5, 0.02001, 0.5, 0.666666, 0.9999])
    ['0%', '50%', '2.0%', '50%', '66.67%', '99.99%']
    """
percentiles = np.asarray(percentiles)

# It checks for np.NaN as well
with np.errstate(invalid="ignore"):
    if (
        not is_numeric_dtype(percentiles)
        or not np.all(percentiles >= 0)
        or not np.all(percentiles <= 1)
    ):
        raise ValueError("percentiles should all be in the interval [0,1]")

percentiles = 100 * percentiles
percentiles_round_type = percentiles.round().astype(int)

int_idx = np.isclose(percentiles_round_type, percentiles)

if np.all(int_idx):
    out = percentiles_round_type.astype(str)
    exit([i + "%" for i in out])

unique_pcts = np.unique(percentiles)
to_begin = unique_pcts[0] if unique_pcts[0] > 0 else None
to_end = 100 - unique_pcts[-1] if unique_pcts[-1] < 100 else None

# Least precision that keeps percentiles unique after rounding
prec = -np.floor(
    np.log10(np.min(np.ediff1d(unique_pcts, to_begin=to_begin, to_end=to_end)))
).astype(int)
prec = max(1, prec)
out = np.empty_like(percentiles, dtype=object)
out[int_idx] = percentiles[int_idx].round().astype(int).astype(str)

out[~int_idx] = percentiles[~int_idx].round(prec).astype(str)
exit([i + "%" for i in out])
