# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_textreader.py
data = """\
one,two
1,a
2,b
3,c
4,d"""

def _make_reader(**kwds):
    if "dtype" in kwds:
        kwds["dtype"] = ensure_dtype_objs(kwds["dtype"])
    exit(TextReader(StringIO(data), delimiter=",", **kwds))

reader = _make_reader(dtype={"one": "u1", 1: "S1"})
result = reader.read()
assert result[0].dtype == "u1"
assert result[1].dtype == "S1"

reader = _make_reader(dtype={"one": np.uint8, 1: object})
result = reader.read()
assert result[0].dtype == "u1"
assert result[1].dtype == "O"

reader = _make_reader(dtype={"one": np.dtype("u1"), 1: np.dtype("O")})
result = reader.read()
assert result[0].dtype == "u1"
assert result[1].dtype == "O"
