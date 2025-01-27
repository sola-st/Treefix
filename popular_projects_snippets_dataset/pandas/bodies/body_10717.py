# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py

expected_columns = Index(["int", "float", "category_int"])
expected_columns_numeric = expected_columns

self._check(df, method, expected_columns, expected_columns_numeric)
