# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_concat.py
# GH 45888: test raise for concat DataFrames with duplicate indices
# https://github.com/pandas-dev/pandas/issues/36263
df1 = DataFrame(np.random.randn(5), index=[0, 1, 2, 3, 3], columns=["a"])
df2 = DataFrame(np.random.randn(5), index=[0, 1, 2, 2, 4], columns=["b"])
msg = "Reindexing only valid with uniquely valued Index objects"
with pytest.raises(InvalidIndexError, match=msg):
    concat([df1, df2], axis=1)
