# Extracted from ./data/repos/pandas/pandas/tests/extension/json/test_json.py
"""
        This fails when we get to tm.assert_series_equal when left.index
        contains dictionaries, which are not hashable.
        """
super().test_groupby_extension_no_sort()
