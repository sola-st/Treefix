# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/methods/test_astype.py
arr = period_range("2000", periods=2, name="idx")

with pytest.raises(TypeError, match=r"Do obj.astype\('int64'\)"):
    arr.astype("uint64")
with pytest.raises(TypeError, match=r"Do obj.astype\('int64'\)"):
    arr.astype("uint32")
