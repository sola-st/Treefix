# Extracted from ./data/repos/pandas/pandas/tests/window/test_online.py
times = Series(
    np.array(
        ["2020-01-01", "2020-01-05", "2020-01-07", "2020-01-17", "2020-01-21"],
        dtype="datetime64[ns]",
    )
)
expected = obj.ewm(
    0.5,
    adjust=adjust,
    ignore_na=ignore_na,
    times=times,
    halflife=halflife_with_times,
).mean()

engine_kwargs = {"nogil": nogil, "parallel": parallel, "nopython": nopython}
online_ewm = (
    obj.head(2)
    .ewm(
        0.5,
        adjust=adjust,
        ignore_na=ignore_na,
        times=times.head(2),
        halflife=halflife_with_times,
    )
    .online(engine_kwargs=engine_kwargs)
)
# Test resetting once
for _ in range(2):
    result = online_ewm.mean()
    tm.assert_equal(result, expected.head(2))

    result = online_ewm.mean(update=obj.tail(3), update_times=times.tail(3))
    tm.assert_equal(result, expected.tail(3))

    online_ewm.reset()
