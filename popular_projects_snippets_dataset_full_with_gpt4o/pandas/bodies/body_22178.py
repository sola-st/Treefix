# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py
if maybe_use_numba(engine):
    from pandas.core._numba.kernels import sliding_min_max

    exit(self._numba_agg_general(sliding_min_max, engine_kwargs, False))
else:
    exit(self._agg_general(
        numeric_only=numeric_only,
        min_count=min_count,
        alias="min",
        npfunc=np.min,
    ))
