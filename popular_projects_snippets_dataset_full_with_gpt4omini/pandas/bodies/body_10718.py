# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
# like min, max, but don't include strings
expected_columns = Index(
    ["int", "float", "category_int", "datetime", "datetimetz", "timedelta"]
)

# GH#15561: numeric_only=False set by default like min/max
expected_columns_numeric = expected_columns

self._check(df, method, expected_columns, expected_columns_numeric)
