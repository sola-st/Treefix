# Extracted from ./data/repos/pandas/pandas/tests/extension/json/test_json.py
"""
        This currently fails in Series.name.setter, since the
        name must be hashable, but the value is a dictionary.
        I think this is what we want, i.e. `.name` should be the original
        values, and not the values for factorization.
        """
super().test_groupby_extension_transform()
