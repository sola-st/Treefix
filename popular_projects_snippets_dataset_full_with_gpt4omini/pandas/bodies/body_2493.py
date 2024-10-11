# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
# GH#13822, incorrect error string with non-unique columns when missing
# column is accessed
df = DataFrame({"x": [1.0], "y": [2.0], "z": [3.0]})
df.columns = ["x", "x", "z"]

# Check that we get the correct value in the KeyError
with pytest.raises(KeyError, match=r"\['y'\] not in index"):
    df[["x", "y", "z"]]
