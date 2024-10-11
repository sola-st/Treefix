# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_records.py
# GH#13937
dr = date_range("2016-01-01", periods=10, freq="S", tz=tz)

df = DataFrame({"datetime": dr}, index=dr)

expected = df.to_records()
result = df.tz_convert("UTC").to_records()

# both converted to UTC, so they are equal
tm.assert_numpy_array_equal(result, expected)
