# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_series_info.py
dtypes = [
    "int64",
    "float64",
    "datetime64[ns]",
    "timedelta64[ns]",
    "complex128",
    "object",
    "bool",
]
n = 10
for dtype in dtypes:
    s = Series(np.random.randint(2, size=n).astype(dtype))
    buf = StringIO()
    s.info(buf=buf)
    res = buf.getvalue()
    name = f"{n:d} non-null     {dtype}"
    assert name in res
