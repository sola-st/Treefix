# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_csv.py

with tm.ensure_clean("csv_date_format_with_dst") as path:
    # make sure we are not failing on transitions
    times = date_range(
        "2013-10-26 23:00",
        "2013-10-27 01:00",
        tz="Europe/London",
        freq="H",
        ambiguous="infer",
    )
    i = times + td
    i = i._with_freq(None)  # freq is not preserved by read_csv
    time_range = np.array(range(len(i)), dtype="int64")
    df = DataFrame({"A": time_range}, index=i)
    df.to_csv(path, index=True)
    # we have to reconvert the index as we
    # don't parse the tz's
    result = read_csv(path, index_col=0)
    result.index = to_datetime(result.index, utc=True).tz_convert(
        "Europe/London"
    )
    tm.assert_frame_equal(result, df)
