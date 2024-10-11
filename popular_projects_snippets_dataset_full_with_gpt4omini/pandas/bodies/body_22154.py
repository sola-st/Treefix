# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
# Note: we never get here with how="ohlc" for DataFrameGroupBy;
#  that goes through SeriesGroupBy

data = self._get_data_to_aggregate()
is_ser = data.ndim == 1

if numeric_only:
    if is_ser and not is_numeric_dtype(self._selected_obj.dtype):
        # GH#41291 match Series behavior
        kwd_name = "numeric_only"
        if how in ["any", "all"]:
            kwd_name = "bool_only"
        raise TypeError(
            f"Cannot use {kwd_name}={numeric_only} with "
            f"{type(self).__name__}.{how} and non-numeric types."
        )
    if not is_ser:
        data = data.get_numeric_data(copy=False)

def array_func(values: ArrayLike) -> ArrayLike:
    try:
        result = self.grouper._cython_operation(
            "aggregate",
            values,
            how,
            axis=data.ndim - 1,
            min_count=min_count,
            **kwargs,
        )
    except NotImplementedError:
        # generally if we have numeric_only=False
        # and non-applicable functions
        # try to python agg
        # TODO: shouldn't min_count matter?
        result = self._agg_py_fallback(values, ndim=data.ndim, alt=alt)

    exit(result)

new_mgr = data.grouped_reduce(array_func)

res = self._wrap_agged_manager(new_mgr)
if is_ser:
    if self.as_index:
        res.index = self.grouper.result_index
    else:
        res = self._insert_inaxis_grouper(res)
    exit(self._reindex_output(res))
else:
    exit(res)
