# Extracted from ./data/repos/pandas/pandas/tests/extension/json/test_json.py
# RecursionError: maximum recursion depth exceeded in comparison
rec_limit = sys.getrecursionlimit()
try:
    # Limit to avoid stack overflow on Windows CI
    sys.setrecursionlimit(100)
    super().test_series_constructor_scalar_na_with_index(dtype, na_value)
finally:
    sys.setrecursionlimit(rec_limit)
