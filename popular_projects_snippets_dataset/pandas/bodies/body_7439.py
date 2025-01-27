# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_names.py
# GH#20421
mi = MultiIndex.from_arrays([[1, 2], [3, 4]], names=["x", "y"])
with pytest.raises(TypeError, match="Can not pass level for dictlike `names`."):
    mi.set_names(names={"x": "z"}, level={"x": "z"})
