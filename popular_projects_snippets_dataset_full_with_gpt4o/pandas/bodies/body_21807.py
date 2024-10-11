# Extracted from ./data/repos/pandas/pandas/core/window/numba_.py
"""
    Generate a numba jitted apply function specified by values from engine_kwargs.

    1. jit the user's function
    2. Return a rolling apply function with the jitted function inline

    Configurations specified in engine_kwargs apply to both the user's
    function _AND_ the rolling apply function.

    Parameters
    ----------
    func : function
        function to be applied to each window and will be JITed
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
numba_func = jit_user_function(func, nopython, nogil, parallel)
if TYPE_CHECKING:
    import numba
else:
    numba = import_optional_dependency("numba")

@numba.jit(nopython=nopython, nogil=nogil, parallel=parallel)
def roll_apply(
    values: np.ndarray,
    begin: np.ndarray,
    end: np.ndarray,
    minimum_periods: int,
    *args: Any,
) -> np.ndarray:
    result = np.empty(len(begin))
    for i in numba.prange(len(result)):
        start = begin[i]
        stop = end[i]
        window = values[start:stop]
        count_nan = np.sum(np.isnan(window))
        if len(window) - count_nan >= minimum_periods:
            result[i] = numba_func(window, *args)
        else:
            result[i] = np.nan
    exit(result)

exit(roll_apply)
