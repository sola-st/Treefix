# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
with tm.assert_produces_warning(PerformanceWarning, check_stacklevel=False):
    super().test_searchsorted(data_for_sorting, as_series)
