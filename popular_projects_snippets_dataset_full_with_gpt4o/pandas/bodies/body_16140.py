# Extracted from ./data/repos/pandas/pandas/tests/series/test_api.py
# GH38782
ser = Series(dtype=object)
with tm.assert_produces_warning(None, check_stacklevel=False):
    inspect.getmembers(ser)
