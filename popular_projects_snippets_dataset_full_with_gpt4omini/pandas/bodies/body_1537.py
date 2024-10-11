# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#25495
df = DataFrame({"Alpha": ["a"], "Numeric": [0]})
categories = Categorical(df["Alpha"], categories=["a", "b", "c"])

# pre-2.0 this swapped in a new array, in 2.0 it operates inplace,
#  consistent with non-split-path
df.loc[:, "Alpha"] = categories

result = df["Alpha"]
expected = Series(categories, index=df.index, name="Alpha").astype(object)
tm.assert_series_equal(result, expected)

# double-check that the non-loc setting retains categoricalness
df["Alpha"] = categories
tm.assert_series_equal(df["Alpha"], Series(categories, name="Alpha"))
