# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_scalar.py
# GH#32809 .iat calls go through DataFrame._get_value, should not
#  call maybe_box_datetimelike
dti = date_range("2016-01-01", periods=3)
tdi = dti - dti
ser = Series(dti.to_pydatetime(), dtype=object)
ser2 = Series(tdi.to_pytimedelta(), dtype=object)
df = DataFrame({"A": ser, "B": ser2})
assert (df.dtypes == object).all()

for result in [df.at[0, "A"], df.iat[0, 0], df.loc[0, "A"], df.iloc[0, 0]]:
    assert result is ser[0]
    assert isinstance(result, datetime)
    assert not isinstance(result, Timestamp)

for result in [df.at[1, "B"], df.iat[1, 1], df.loc[1, "B"], df.iloc[1, 1]]:
    assert result is ser2[1]
    assert isinstance(result, timedelta)
    assert not isinstance(result, Timedelta)
