# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH35439
data = [[4, 2], [3, 2], [4, 3]]
cols = ["aaaaaaaaa", "b"]
df = DataFrame(data, columns=cols)
df_cat_cols = DataFrame(data, columns=pd.CategoricalIndex(cols))

assert df.to_string() == df_cat_cols.to_string()
