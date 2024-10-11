# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reindex.py
# GH 40980
ser = Series([1, 2])
with pytest.raises(
    TypeError, match=r"Only one positional argument \('index'\) is allowed"
):
    ser.reindex([2, 3], False)
