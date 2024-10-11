# Extracted from ./data/repos/pandas/pandas/tests/series/test_constructors.py
# gh-15869
for arr in [
    np.array([None, None, None, None, datetime.now(), None]),
    np.array([None, None, datetime.now(), None]),
]:
    result = Series(arr)
    assert result.dtype == "M8[ns]"
