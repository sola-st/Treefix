# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py

# 10170
# make sure that we are consistently display date formatting
x = Series(date_range("20130101 09:00:00", periods=5, freq="D"))
x.iloc[1] = np.nan
result = fmt.Datetime64Formatter(x).get_result()
assert result[0].strip() == "2013-01-01 09:00:00"
assert result[1].strip() == "NaT"
assert result[4].strip() == "2013-01-05 09:00:00"

x = Series(date_range("20130101 09:00:00", periods=5, freq="s"))
x.iloc[1] = np.nan
result = fmt.Datetime64Formatter(x).get_result()
assert result[0].strip() == "2013-01-01 09:00:00"
assert result[1].strip() == "NaT"
assert result[4].strip() == "2013-01-01 09:00:04"

x = Series(date_range("20130101 09:00:00", periods=5, freq="ms"))
x.iloc[1] = np.nan
result = fmt.Datetime64Formatter(x).get_result()
assert result[0].strip() == "2013-01-01 09:00:00.000"
assert result[1].strip() == "NaT"
assert result[4].strip() == "2013-01-01 09:00:00.004"

x = Series(date_range("20130101 09:00:00", periods=5, freq="us"))
x.iloc[1] = np.nan
result = fmt.Datetime64Formatter(x).get_result()
assert result[0].strip() == "2013-01-01 09:00:00.000000"
assert result[1].strip() == "NaT"
assert result[4].strip() == "2013-01-01 09:00:00.000004"

x = Series(date_range("20130101 09:00:00", periods=5, freq="N"))
x.iloc[1] = np.nan
result = fmt.Datetime64Formatter(x).get_result()
assert result[0].strip() == "2013-01-01 09:00:00.000000000"
assert result[1].strip() == "NaT"
assert result[4].strip() == "2013-01-01 09:00:00.000000004"
