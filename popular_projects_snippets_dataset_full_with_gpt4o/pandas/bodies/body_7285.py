# Extracted from ./data/repos/pandas/pandas/tests/indexes/timedeltas/methods/test_astype.py
arr = timedelta_range("1H", periods=2)

with pytest.raises(TypeError, match=r"Do obj.astype\('int64'\)"):
    arr.astype("uint64")
with pytest.raises(TypeError, match=r"Do obj.astype\('int64'\)"):
    arr.astype("uint32")
