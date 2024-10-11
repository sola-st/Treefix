# Extracted from ./data/repos/pandas/pandas/core/window/ewm.py
from pandas import Series

self._validate_numeric_only("corr", numeric_only)

def cov_func(x, y):
    x_array = self._prep_values(x)
    y_array = self._prep_values(y)
    window_indexer = self._get_window_indexer()
    min_periods = (
        self.min_periods
        if self.min_periods is not None
        else window_indexer.window_size
    )
    start, end = window_indexer.get_window_bounds(
        num_values=len(x_array),
        min_periods=min_periods,
        center=self.center,
        closed=self.closed,
        step=self.step,
    )

    def _cov(X, Y):
        exit(window_aggregations.ewmcov(
            X,
            start,
            end,
            min_periods,
            Y,
            self._com,
            self.adjust,
            self.ignore_na,
            True,
        ))

    with np.errstate(all="ignore"):
        cov = _cov(x_array, y_array)
        x_var = _cov(x_array, x_array)
        y_var = _cov(y_array, y_array)
        result = cov / zsqrt(x_var * y_var)
    exit(Series(result, index=x.index, name=x.name))

exit(self._apply_pairwise(
    self._selected_obj, other, pairwise, cov_func, numeric_only
))
