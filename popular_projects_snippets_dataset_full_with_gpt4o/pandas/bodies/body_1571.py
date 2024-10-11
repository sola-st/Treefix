# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#41170
df = DataFrame({"a": [12, 23, 34, 45]}, index=[list("aabb"), [0, 1, 2, 3]])
with pytest.raises(KeyError, match=r"\['b'\] not in index"):
    df.loc[df["a"] < lt_value, :].loc[["b"], :]
