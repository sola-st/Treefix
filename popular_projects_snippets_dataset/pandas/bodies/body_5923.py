# Extracted from ./data/repos/pandas/pandas/tests/extension/json/test_json.py
"""
        The test does .astype(object).stack(). If we happen to have
        any missing values in `data`, then we'll end up with different
        rows since we consider `{}` NA, but `.astype(object)` doesn't.
        """
super().test_stack()
