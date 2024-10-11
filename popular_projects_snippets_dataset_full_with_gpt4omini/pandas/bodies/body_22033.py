# Extracted from ./data/repos/pandas/pandas/core/groupby/numba_.py
"""
    Generate a numba jitted agg function specified by values from engine_kwargs.

    1. jit the user's function
    2. Return a groupby agg function with the jitted function inline

    Configurations specified in engine_kwargs apply to both the user's
    function _AND_ the groupby evaluation loop.

    Parameters
    ----------
    func : function
        function to be applied to each group and will be JITed
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
def group_agg(
    values: np.ndarray,
    index: np.ndarray,
    begin: np.ndarray,
    end: np.ndarray,
    num_columns: int,
    *args: Any,
) -> np.ndarray:

    assert len(begin) == len(end)
    num_groups = len(begin)

    result = np.empty((num_groups, num_columns))
    for i in numba.prange(num_groups):
        group_index = index[begin[i] : end[i]]
        for j in numba.prange(num_columns):
            group = values[begin[i] : end[i], j]
            result[i, j] = numba_func(group, group_index, *args)
    exit(result)

exit(group_agg)
