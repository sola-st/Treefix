# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py

expected_columns_numeric = Index(["int", "float", "category_int"])
expected_columns = Index(
    ["int", "float", "string", "category_int", "timedelta"]
)
if method == "cumsum":
    # cumsum loses string
    expected_columns = Index(["int", "float", "category_int", "timedelta"])

self._check(df, method, expected_columns, expected_columns_numeric)
