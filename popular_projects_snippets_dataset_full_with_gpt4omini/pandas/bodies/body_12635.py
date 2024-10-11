# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_pandas.py
# GH 13774
values = [
    [b"E\xc9, 17", b"", b"a", b"b", b"c"],
    [b"E\xc9, 17", b"a", b"b", b"c"],
    [b"EE, 17", b"", b"a", b"b", b"c"],
    [b"E\xc9, 17", b"\xf8\xfc", b"a", b"b", b"c"],
    [b"", b"a", b"b", b"c"],
    [b"\xf8\xfc", b"a", b"b", b"c"],
    [b"A\xf8\xfc", b"", b"a", b"b", b"c"],
    [np.nan, b"", b"b", b"c"],
    [b"A\xf8\xfc", np.nan, b"", b"b", b"c"],
]

values = [
    [x.decode("latin-1") if isinstance(x, bytes) else x for x in y]
    for y in values
]

examples = []
for dtype in ["category", object]:
    for val in values:
        examples.append(Series(val, dtype=dtype))

def roundtrip(s, encoding="latin-1"):
    with tm.ensure_clean("test.json") as path:
        s.to_json(path, encoding=encoding)
        retr = read_json(path, encoding=encoding)
        tm.assert_series_equal(s, retr, check_categorical=False)

for s in examples:
    roundtrip(s)
