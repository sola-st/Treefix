# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_dict.py
# GH#18372 When converting to dict with orient='records' columns of
# datetime that are tz-aware were not converted to required arrays
data = [
    (datetime(2017, 11, 18, 21, 53, 0, 219225, tzinfo=pytz.utc),),
    (datetime(2017, 11, 18, 22, 6, 30, 61810, tzinfo=pytz.utc),),
]
df = DataFrame(list(data), columns=["d"])

result = df.to_dict(orient="records")
expected = [
    {"d": Timestamp("2017-11-18 21:53:00.219225+0000", tz=pytz.utc)},
    {"d": Timestamp("2017-11-18 22:06:30.061810+0000", tz=pytz.utc)},
]
tm.assert_dict_equal(result[0], expected[0])
tm.assert_dict_equal(result[1], expected[1])
