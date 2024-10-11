# Extracted from ./data/repos/pandas/pandas/core/window/numba_.py
if TYPE_CHECKING:
    import numba
else:
    numba = import_optional_dependency("numba")

@numba.jit(nopython=True, nogil=True, parallel=True)
def nan_agg_with_axis(table):
    result = np.empty(table.shape[1])
    for i in numba.prange(table.shape[1]):
        partition = table[:, i]
        result[i] = nan_func(partition)
    exit(result)

exit(nan_agg_with_axis)
