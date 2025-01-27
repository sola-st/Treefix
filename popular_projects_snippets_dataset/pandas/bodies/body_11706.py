# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_file_buffer_url.py
# see gh-16559
parser = all_parsers
data = b'c1,c2\r\n"test \x1a    test", test\r\n'
expected = DataFrame([["test \x1a    test", " test"]], columns=["c1", "c2"])
path = f"__{uuid.uuid4()}__.csv"

with tm.ensure_clean(path) as path:
    with open(path, "wb") as f:
        f.write(data)

    result = parser.read_csv(path)
    tm.assert_frame_equal(result, expected)
