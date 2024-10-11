# Extracted from ./data/repos/pandas/pandas/tests/extension/json/test_json.py
# TypeError: All values must be of type <class 'collections.abc.Mapping'>
rec_limit = sys.getrecursionlimit()
try:
    # Limit to avoid stack overflow on Windows CI
    sys.setrecursionlimit(100)
    super().test_series_constructor_scalar_with_index(data, dtype)
finally:
    sys.setrecursionlimit(rec_limit)
