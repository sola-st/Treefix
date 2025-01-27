# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
df = datetime_frame
df["date"] = Timestamp("20130101 20:43:42")
dl = df.columns.get_loc("date")
df.iloc[1, dl] = Timestamp("19710101 20:43:42")
df.iloc[2, dl] = Timestamp("21460101 20:43:42")
df.iloc[4, dl] = pd.NaT

json = df.to_json(date_format="epoch", date_unit=unit)

# force date unit
result = read_json(json, date_unit=unit)
tm.assert_frame_equal(result, df)

# detect date unit
result = read_json(json, date_unit=None)
tm.assert_frame_equal(result, df)
