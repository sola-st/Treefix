# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_encoding.py
# see gh-31819
parser = all_parsers
encoding = "shift-jis"

title = "てすと"
data = "こむ"

expected = DataFrame({title: [data]})

with tempfile.NamedTemporaryFile() as f:
    f.write(f"{title}\n{data}".encode(encoding))

    f.seek(0)

    result = parser.read_csv(f, encoding=encoding)
    tm.assert_frame_equal(result, expected)
    assert not f.closed
