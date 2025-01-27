# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
df = datetime_frame

df["date"] = Timestamp(date)
df.iloc[1, df.columns.get_loc("date")] = pd.NaT
df.iloc[5, df.columns.get_loc("date")] = pd.NaT
if date_unit:
    json = df.to_json(date_format="iso", date_unit=date_unit)
else:
    json = df.to_json(date_format="iso")
result = read_json(json)
expected = df.copy()
tm.assert_frame_equal(result, expected)
