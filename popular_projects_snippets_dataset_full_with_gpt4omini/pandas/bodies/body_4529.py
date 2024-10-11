# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH#44091
dti = date_range("2016-01-01", periods=3)

ser1 = Series(range(3), index=dti)
ser2 = Series(range(3), index=dti.tz_localize("UTC"))
ser3 = Series(range(3), index=dti.tz_localize("US/Central"))
ser4 = Series(range(3))

# no tz-naive, but we do have mixed tzs and a non-DTI
df1 = DataFrame({"A": ser2, "B": ser3, "C": ser4})
exp_index = Index(
    list(ser2.index) + list(ser3.index) + list(ser4.index), dtype=object
)
tm.assert_index_equal(df1.index, exp_index)

df2 = DataFrame({"A": ser2, "C": ser4, "B": ser3})
exp_index3 = Index(
    list(ser2.index) + list(ser4.index) + list(ser3.index), dtype=object
)
tm.assert_index_equal(df2.index, exp_index3)

df3 = DataFrame({"B": ser3, "A": ser2, "C": ser4})
exp_index3 = Index(
    list(ser3.index) + list(ser2.index) + list(ser4.index), dtype=object
)
tm.assert_index_equal(df3.index, exp_index3)

df4 = DataFrame({"C": ser4, "B": ser3, "A": ser2})
exp_index4 = Index(
    list(ser4.index) + list(ser3.index) + list(ser2.index), dtype=object
)
tm.assert_index_equal(df4.index, exp_index4)

# TODO: not clear if these raising is desired (no extant tests),
#  but this is de facto behavior 2021-12-22
msg = "Cannot join tz-naive with tz-aware DatetimeIndex"
with pytest.raises(TypeError, match=msg):
    DataFrame({"A": ser2, "B": ser3, "C": ser4, "D": ser1})
with pytest.raises(TypeError, match=msg):
    DataFrame({"A": ser2, "B": ser3, "D": ser1})
with pytest.raises(TypeError, match=msg):
    DataFrame({"D": ser1, "A": ser2, "B": ser3})
