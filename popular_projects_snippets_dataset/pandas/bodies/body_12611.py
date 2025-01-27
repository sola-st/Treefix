# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
td = timedelta(23)
ts = Timestamp("20130101")
frame = DataFrame({"a": [td, ts]}, dtype=object)

expected = DataFrame(
    {"a": [pd.Timedelta(td).as_unit("ns").value, ts.as_unit("ns").value]}
)
result = read_json(frame.to_json(date_unit="ns"), dtype={"a": "int64"})
tm.assert_frame_equal(result, expected, check_index_type=False)
