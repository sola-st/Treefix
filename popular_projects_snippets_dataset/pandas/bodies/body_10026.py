# Extracted from ./data/repos/pandas/pandas/tests/window/test_online.py
expected = obj.ewm(0.5, adjust=adjust, ignore_na=ignore_na).mean()
engine_kwargs = {"nogil": nogil, "parallel": parallel, "nopython": nopython}

online_ewm = (
    obj.head(2)
    .ewm(0.5, adjust=adjust, ignore_na=ignore_na)
    .online(engine_kwargs=engine_kwargs)
)
# Test resetting once
for _ in range(2):
    result = online_ewm.mean()
    tm.assert_equal(result, expected.head(2))

    result = online_ewm.mean(update=obj.tail(3))
    tm.assert_equal(result, expected.tail(3))

    online_ewm.reset()
