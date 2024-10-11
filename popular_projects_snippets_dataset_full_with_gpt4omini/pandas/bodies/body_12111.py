# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_encoding.py
# see gh-2298
parser = all_parsers
data = """skip this
skip this too
A,B,C
1,2,3
4,5,6""".replace(
    ",", sep
)
path = f"__{uuid.uuid4()}__.csv"
kwargs = {"sep": sep, "skiprows": 2}
utf8 = "utf-8"

with tm.ensure_clean(path) as path:
    bytes_data = data.encode(encoding)

    with open(path, "wb") as f:
        f.write(bytes_data)

    with TextIOWrapper(BytesIO(data.encode(utf8)), encoding=utf8) as bytes_buffer:
        result = parser.read_csv(path, encoding=encoding, **kwargs)
        expected = parser.read_csv(bytes_buffer, encoding=utf8, **kwargs)
    tm.assert_frame_equal(result, expected)
