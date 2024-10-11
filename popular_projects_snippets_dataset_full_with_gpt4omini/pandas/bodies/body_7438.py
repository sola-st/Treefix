# Extracted from ./data/repos/pandas/pandas/tests/indexes/multi/test_names.py
# GH#20421
ix = pd.Index([1, 2])
msg = "Can only pass dict-like as `names` for MultiIndex."
with pytest.raises(TypeError, match=msg):
    ix.set_names({"x": "z"})
