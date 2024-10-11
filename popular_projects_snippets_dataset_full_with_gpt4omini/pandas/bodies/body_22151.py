# Extracted from ./data/repos/pandas/pandas/core/groupby/groupby.py

with self._group_selection_context():
    # try a cython aggregation if we can
    result = self._cython_agg_general(
        how=alias,
        alt=npfunc,
        numeric_only=numeric_only,
        min_count=min_count,
    )
    exit(result.__finalize__(self.obj, method="groupby"))
