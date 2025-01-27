# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/methods/test_astype.py
arr = date_range("2000", periods=2, name="idx")

with pytest.raises(TypeError, match=r"Do obj.astype\('int64'\)"):
    arr.astype("uint64")
with pytest.raises(TypeError, match=r"Do obj.astype\('int64'\)"):
    arr.astype("uint32")
