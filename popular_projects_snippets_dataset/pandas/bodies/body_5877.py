# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
with tm.assert_produces_warning(PerformanceWarning, check_stacklevel=False):
    super().test_fillna_limit_pad(data_missing)
