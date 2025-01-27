# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
# GH#18308
start = Timestamp("2017-10-29 00:00:00+0200", tz="Europe/Madrid")
end = Timestamp("2017-10-29 03:00:00+0100", tz="Europe/Madrid")
ts = Timestamp("2016-10-10 03:00:00", tz="Europe/Madrid")
idx = date_range(start, end, inclusive="left", freq="H")
assert ts not in idx  # i.e. result.loc setitem is with-expansion

result = DataFrame(index=idx, columns=["value"])
result.loc[ts, "value"] = 12
expected = DataFrame(
    [np.nan] * len(idx) + [12],
    index=idx.append(DatetimeIndex([ts])),
    columns=["value"],
    dtype=object,
)
tm.assert_frame_equal(result, expected)
