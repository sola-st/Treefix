# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_getitem.py
# GH#29189 float_index.get_loc(None) should raise KeyError, not TypeError
ser = Series([2, 5, 6, 8], index=[2.0, 4.0, 4.0, 5.0])
with pytest.raises(KeyError, match="None"):
    ser[None]

with pytest.raises(KeyError, match="None"):
    ser.index.get_loc(None)

with pytest.raises(KeyError, match="None"):
    ser.index._engine.get_loc(None)
