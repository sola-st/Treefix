# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_python_parser_only.py
# see gh-6607
parser = python_parser_only

with open(csv1, "rb") as f:
    data = f.read()

data = data.replace(b",", b"::")
expected = parser.read_csv(csv1)

module = pytest.importorskip(compression)
klass = getattr(module, klass)

with tm.ensure_clean() as path:
    with klass(path, mode="wb") as tmp:
        tmp.write(data)

    result = parser.read_csv(path, sep="::", compression=compression)
    tm.assert_frame_equal(result, expected)
