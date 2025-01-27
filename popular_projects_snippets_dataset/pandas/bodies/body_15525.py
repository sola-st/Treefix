# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_rename_axis.py
# GH 19978
mi = MultiIndex.from_product([["a", "b", "c"], [1, 2]], names=["ll", "nn"])
ser = Series(list(range(len(mi))), index=mi)

result = ser.rename_axis(index={"ll": "foo"})
assert result.index.names == ["foo", "nn"]

result = ser.rename_axis(index=str.upper, axis=0)
assert result.index.names == ["LL", "NN"]

result = ser.rename_axis(index=["foo", "goo"])
assert result.index.names == ["foo", "goo"]

with pytest.raises(TypeError, match="unexpected"):
    ser.rename_axis(columns="wrong")
