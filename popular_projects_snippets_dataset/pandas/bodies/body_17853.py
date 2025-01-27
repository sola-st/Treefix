# Extracted from ./data/repos/pandas/pandas/tests/util/test_assert_frame_equal.py
# GH#50323
df1 = DataFrame({"a": pd.Series([pd.NA, 1], dtype="Int64")})
df2 = DataFrame({"a": pd.Series([1, 1], dtype="Int64")})

msg = r'DataFrame.iloc\[:, 0\] \(column name="a"\) NA mask values are different'
with pytest.raises(AssertionError, match=msg):
    tm.assert_frame_equal(df1, df2)
