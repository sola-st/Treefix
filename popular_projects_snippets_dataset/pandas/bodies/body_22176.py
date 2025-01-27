# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
if maybe_use_numba(engine):
    from pandas.core._numba.kernels import sliding_sum

    exit(self._numba_agg_general(
        sliding_sum,
        engine_kwargs,
    ))
else:
    # If we are grouping on categoricals we want unobserved categories to
    # return zero, rather than the default of NaN which the reindexing in
    # _agg_general() returns. GH #31422
    with com.temp_setattr(self, "observed", True):
        result = self._agg_general(
            numeric_only=numeric_only,
            min_count=min_count,
            alias="sum",
            npfunc=np.sum,
        )

    exit(self._reindex_output(result, fill_value=0))
