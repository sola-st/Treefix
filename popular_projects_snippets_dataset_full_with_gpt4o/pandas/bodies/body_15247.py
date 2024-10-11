# Extracted from ./data/repos/pandas/pandas/tests/series/indexing/test_xs.py
# GH#41760
mi = MultiIndex.from_tuples([("a", "x")], names=["level1", "level2"])
ser = Series([1], index=mi)
with pytest.raises(TypeError, match="list keys are not supported"):
    ser.xs(["a", "x"], axis=0, drop_level=False)

with pytest.raises(TypeError, match="list keys are not supported"):
    ser.xs(["a"], axis=0, drop_level=False)
