# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_indexing.py
# GH#34240
pi = period_range("2000", periods=3, name="A")
with pytest.raises(KeyError, match="A"):
    pi.get_loc("A")

ser = Series([1, 2, 3], index=pi)
with pytest.raises(KeyError, match="A"):
    ser.loc["A"]

with pytest.raises(KeyError, match="A"):
    ser["A"]

assert "A" not in ser
assert "A" not in pi
