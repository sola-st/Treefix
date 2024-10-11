# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
# Make sure plot defaults to rcParams['axes.grid'] setting, GH 9792
self._check_grid_settings(
    Series([1, 2, 3]),
    plotting.PlotAccessor._series_kinds + plotting.PlotAccessor._common_kinds,
)
