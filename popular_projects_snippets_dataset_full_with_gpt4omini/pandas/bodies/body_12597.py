# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py

# frame
df = datetime_frame
df["date"] = Timestamp("20130101")

json = df.to_json()
result = read_json(json)
tm.assert_frame_equal(result, df)

df["foo"] = 1.0
json = df.to_json(date_unit="ns")

result = read_json(json, convert_dates=False)
expected = df.copy()
expected["date"] = expected["date"].values.view("i8")
expected["foo"] = expected["foo"].astype("int64")
tm.assert_frame_equal(result, expected)

# series
ts = Series(Timestamp("20130101"), index=datetime_series.index)
json = ts.to_json()
result = read_json(json, typ="series")
tm.assert_series_equal(result, ts)
