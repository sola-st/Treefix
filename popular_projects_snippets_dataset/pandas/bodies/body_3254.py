# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# see GH#9757
a = Series(date_range("2010-01-04", periods=5))
b = Series(date_range("3/6/2012 00:00", periods=5, tz="US/Eastern"))
c = Series([Timedelta(x, unit="d") for x in range(5)])
d = Series(range(5))
e = Series([0.0, 0.2, 0.4, 0.6, 0.8])

df = DataFrame({"a": a, "b": b, "c": c, "d": d, "e": e})

# Datetime-like
result = df.astype(str)

expected = DataFrame(
    {
        "a": list(map(str, map(lambda x: Timestamp(x)._date_repr, a._values))),
        "b": list(map(str, map(Timestamp, b._values))),
        "c": list(map(lambda x: Timedelta(x)._repr_base(), c._values)),
        "d": list(map(str, d._values)),
        "e": list(map(str, e._values)),
    }
)

tm.assert_frame_equal(result, expected)
