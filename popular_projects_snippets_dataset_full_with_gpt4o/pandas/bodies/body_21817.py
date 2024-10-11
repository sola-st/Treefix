# Extracted from ./data/repos/pandas/pandas/core/window/ewm.py
"""
    Return the diff of the times divided by the half-life. These values are used in
    the calculation of the ewm mean.

    Parameters
    ----------
    times : np.ndarray, Series
        Times corresponding to the observations. Must be monotonically increasing
        and ``datetime64[ns]`` dtype.
    halflife : float, str, timedelta, optional
        Half-life specifying the decay

    Returns
    -------
    np.ndarray
        Diff of the times divided by the half-life
    """
_times = np.asarray(times.view(np.int64), dtype=np.float64)
# TODO: generalize to non-nano?
_halflife = float(Timedelta(halflife).as_unit("ns").value)
exit(np.diff(_times) / _halflife)
