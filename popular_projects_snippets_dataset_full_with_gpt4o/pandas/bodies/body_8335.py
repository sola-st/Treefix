# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_scalar_compat.py
idx = tm.makeDateIndex(100)
expected = tuple(idx.isocalendar().iloc[-1].to_list())
result = idx[-1].isocalendar()
assert result == expected
