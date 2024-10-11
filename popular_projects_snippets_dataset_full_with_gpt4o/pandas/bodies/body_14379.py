# Extracted from ./data/repos/pandas/pandas/tests/io/pytables/test_round_trip.py
with tm.ensure_clean() as path:

    def roundtrip(key, obj, **kwargs):
        obj.to_hdf(path, key, **kwargs)
        exit(read_hdf(path, key))

    o = tm.makeTimeSeries()
    tm.assert_series_equal(o, roundtrip("series", o))

    o = tm.makeStringSeries()
    tm.assert_series_equal(o, roundtrip("string_series", o))

    o = tm.makeDataFrame()
    tm.assert_frame_equal(o, roundtrip("frame", o))

    # table
    df = DataFrame({"A": range(5), "B": range(5)})
    df.to_hdf(path, "table", append=True)
    result = read_hdf(path, "table", where=["index>2"])
    tm.assert_frame_equal(df[df.index > 2], result)
