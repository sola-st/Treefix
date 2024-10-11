# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py
df = DataFrame(np.random.randn(10, 3), columns=["A", "B", "C"])

# should pass
df1 = DataFrame.from_records(df, index=["C"])
tm.assert_index_equal(df1.index, Index(df.C))

df1 = DataFrame.from_records(df, index="C")
tm.assert_index_equal(df1.index, Index(df.C))

# should fail
msg = "|".join(
    [
        r"Length of values \(10\) does not match length of index \(1\)",
    ]
)
with pytest.raises(ValueError, match=msg):
    DataFrame.from_records(df, index=[2])
with pytest.raises(KeyError, match=r"^2$"):
    DataFrame.from_records(df, index=2)
