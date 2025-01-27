# Extracted from ./data/repos/pandas/pandas/tests/indexing/multiindex/test_loc.py
# GH#27420 KeyError, not TypeError
df = DataFrame(np.arange(12).reshape(4, 3), columns=["A", "B", "C"])
df2 = df.set_index(["A", "B"])

with pytest.raises(KeyError, match="1"):
    df2.loc[(1, 6)]
