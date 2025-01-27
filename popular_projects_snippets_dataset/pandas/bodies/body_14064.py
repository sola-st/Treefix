# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
# GH19030
# Check that high-precision time values for the end of day are
# included in repr for DatetimeIndex
df = DataFrame({"A": date_range(start=start_date, freq="D", periods=5)})
result = str(df)
assert start_date in result

dti = date_range(start=start_date, freq="D", periods=5)
df = DataFrame({"A": range(5)}, index=dti)
result = str(df.index)
assert start_date in result
