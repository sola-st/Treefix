# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH 29052

timestamps = [
    Timestamp("2019-03-15 12:34:31.909000+0000", tz="UTC"),
    Timestamp("2019-03-15 12:34:34.359000+0000", tz="UTC"),
    Timestamp("2019-03-15 12:34:34.660000+0000", tz="UTC"),
]
df = DataFrame(data=[0, 1, 2], index=timestamps)
result = df.apply(lambda x: x.name, axis=1)
expected = Series(index=timestamps, data=timestamps)

tm.assert_series_equal(result, expected)
