# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_reindex.py
# GH 40980
ser = Series([1, 2])
msg = r"'index' passed as both positional and keyword argument"
with pytest.raises(TypeError, match=msg):
    ser.reindex([2, 3], index=[3, 4])
