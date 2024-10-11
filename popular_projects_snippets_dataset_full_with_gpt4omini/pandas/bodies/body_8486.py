# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_partial_slicing.py
# GH14856
# Test various combinations of string slicing resolution vs.
# index resolution
# - If string resolution is less precise than index resolution,
# string is considered a slice
# - If string resolution is equal to or more precise than index
# resolution, string is considered an exact match
formats = [
    "%Y",
    "%Y-%m",
    "%Y-%m-%d",
    "%Y-%m-%d %H",
    "%Y-%m-%d %H:%M",
    "%Y-%m-%d %H:%M:%S",
]
resolutions = ["year", "month", "day", "hour", "minute", "second"]
for rnum, resolution in enumerate(resolutions[2:], 2):
    # we check only 'day', 'hour', 'minute' and 'second'
    unit = Timedelta("1 " + resolution)
    middate = datetime(2012, 1, 1, 0, 0, 0)
    index = DatetimeIndex([middate - unit, middate, middate + unit])
    values = [1, 2, 3]
    df = DataFrame({"a": values}, index, dtype=np.int64)
    assert df.index.resolution == resolution

    # Timestamp with the same resolution as index
    # Should be exact match for Series (return scalar)
    # and raise KeyError for Frame
    for timestamp, expected in zip(index, values):
        ts_string = timestamp.strftime(formats[rnum])
        # make ts_string as precise as index
        result = df["a"][ts_string]
        assert isinstance(result, np.int64)
        assert result == expected
        msg = rf"^'{ts_string}'$"
        with pytest.raises(KeyError, match=msg):
            df[ts_string]

            # Timestamp with resolution less precise than index
    for fmt in formats[:rnum]:
        for element, theslice in [[0, slice(None, 1)], [1, slice(1, None)]]:
            ts_string = index[element].strftime(fmt)

            # Series should return slice
            result = df["a"][ts_string]
            expected = df["a"][theslice]
            tm.assert_series_equal(result, expected)

            # pre-2.0 df[ts_string] was overloaded to interpret this
            #  as slicing along index
            with pytest.raises(KeyError, match=ts_string):
                df[ts_string]

            # Timestamp with resolution more precise than index
            # Compatible with existing key
            # Should return scalar for Series
            # and raise KeyError for Frame
    for fmt in formats[rnum + 1 :]:
        ts_string = index[1].strftime(fmt)
        result = df["a"][ts_string]
        assert isinstance(result, np.int64)
        assert result == 2
        msg = rf"^'{ts_string}'$"
        with pytest.raises(KeyError, match=msg):
            df[ts_string]

            # Not compatible with existing key
            # Should raise KeyError
    for fmt, res in list(zip(formats, resolutions))[rnum + 1 :]:
        ts = index[1] + Timedelta("1 " + res)
        ts_string = ts.strftime(fmt)
        msg = rf"^'{ts_string}'$"
        with pytest.raises(KeyError, match=msg):
            df["a"][ts_string]
        with pytest.raises(KeyError, match=msg):
            df[ts_string]
