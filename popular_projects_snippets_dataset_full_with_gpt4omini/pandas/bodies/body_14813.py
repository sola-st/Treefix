# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# Make sure plot defaults to rcParams['axes.grid'] setting, GH 9792
self._check_grid_settings(
    DataFrame({"a": [1, 2, 3], "b": [2, 3, 4]}),
    plotting.PlotAccessor._dataframe_kinds,
    kws={"x": "a", "y": "b"},
)
