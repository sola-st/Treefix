# Extracted from ./data/repos/pandas/pandas/core/window/online.py
"""
    Generate a numba jitted groupby ewma function specified by values
    from engine_kwargs.

    Parameters
    ----------
    nopython : bool
        nopython to be passed into numba.jit
    nogil : bool
        nogil to be passed into numba.jit
    parallel : bool
        parallel to be passed into numba.jit

    Returns
    -------
    Numba function
    """
if TYPE_CHECKING:
    import numba
else:
    numba = import_optional_dependency("numba")

@numba.jit(nopython=nopython, nogil=nogil, parallel=parallel)
def online_ewma(
    values: np.ndarray,
    deltas: np.ndarray,
    minimum_periods: int,
    old_wt_factor: float,
    new_wt: float,
    old_wt: np.ndarray,
    adjust: bool,
    ignore_na: bool,
):
    """
        Compute online exponentially weighted mean per column over 2D values.

        Takes the first observation as is, then computes the subsequent
        exponentially weighted mean accounting minimum periods.
        """
    result = np.empty(values.shape)
    weighted_avg = values[0]
    nobs = (~np.isnan(weighted_avg)).astype(np.int64)
    result[0] = np.where(nobs >= minimum_periods, weighted_avg, np.nan)

    for i in range(1, len(values)):
        cur = values[i]
        is_observations = ~np.isnan(cur)
        nobs += is_observations.astype(np.int64)
        for j in numba.prange(len(cur)):
            if not np.isnan(weighted_avg[j]):
                if is_observations[j] or not ignore_na:

                    # note that len(deltas) = len(vals) - 1 and deltas[i] is to be
                    # used in conjunction with vals[i+1]
                    old_wt[j] *= old_wt_factor ** deltas[j - 1]
                    if is_observations[j]:
                        # avoid numerical errors on constant series
                        if weighted_avg[j] != cur[j]:
                            weighted_avg[j] = (
                                (old_wt[j] * weighted_avg[j]) + (new_wt * cur[j])
                            ) / (old_wt[j] + new_wt)
                        if adjust:
                            old_wt[j] += new_wt
                        else:
                            old_wt[j] = 1.0
            elif is_observations[j]:
                weighted_avg[j] = cur[j]

        result[i] = np.where(nobs >= minimum_periods, weighted_avg, np.nan)

    exit((result, old_wt))

exit(online_ewma)
