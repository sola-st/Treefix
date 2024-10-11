# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_ujson.py
dtype = np.int64
s = Series(
    [10, 20, 30, 40, 50, 60],
    name="series",
    index=[6, 7, 8, 9, 10, 15],
    dtype=dtype,
).sort_values()
assert s.dtype == dtype

encode_kwargs = {} if orient is None else {"orient": orient}

output = ujson.decode(ujson.encode(s, **encode_kwargs))
assert s.dtype == dtype

if orient == "split":
    dec = _clean_dict(output)
    output = Series(**dec)
else:
    output = Series(output)

if orient in (None, "index"):
    s.name = None
    output = output.sort_values()
    s.index = ["6", "7", "8", "9", "10", "15"]
elif orient in ("records", "values"):
    s.name = None
    s.index = [0, 1, 2, 3, 4, 5]

assert s.dtype == dtype
tm.assert_series_equal(output, s)
