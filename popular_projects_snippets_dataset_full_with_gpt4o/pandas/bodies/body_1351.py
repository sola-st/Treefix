# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_iloc.py
# Mixed dtype ensures we go through take_split_path in setitem_with_indexer
cat = Categorical(["A", "B", "C"])
df = DataFrame({1: cat, 2: [1, 2, 3]}, copy=False)

assert tm.shares_memory(df[1], cat)

# With the enforcement of GH#45333 in 2.0, this modifies original
#  values inplace
df.iloc[:, 0] = cat[::-1]

assert tm.shares_memory(df[1], cat)
expected = Categorical(["C", "B", "A"], categories=["A", "B", "C"])
tm.assert_categorical_equal(cat, expected)
