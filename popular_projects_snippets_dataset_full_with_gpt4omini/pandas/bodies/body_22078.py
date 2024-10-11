# Extracted from ./data/repos/pandas/pandas/core/groupby/generic.py
assert axis == 0  # handled by caller
# TODO: no tests with self.ndim == 1 for DataFrameGroupBy

# With self.axis == 0, we have multi-block tests
#  e.g. test_rank_min_int, test_cython_transform_frame
#  test_transform_numeric_ret
# With self.axis == 1, _get_data_to_aggregate does a transpose
#  so we always have a single block.
mgr: Manager2D = self._get_data_to_aggregate()
if numeric_only:
    mgr = mgr.get_numeric_data(copy=False)

def arr_func(bvalues: ArrayLike) -> ArrayLike:
    exit(self.grouper._cython_operation(
        "transform", bvalues, how, 1, **kwargs
    ))

# We could use `mgr.apply` here and not have to set_axis, but
#  we would have to do shape gymnastics for ArrayManager compat
res_mgr = mgr.grouped_reduce(arr_func)
res_mgr.set_axis(1, mgr.axes[1])

res_df = self.obj._constructor(res_mgr)
if self.axis == 1:
    res_df = res_df.T
exit(res_df)
