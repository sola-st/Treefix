# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_encoding.py
# GH43439
parser = all_parsers
content = b"abcd"
if "t" in mode:
    content = "abcd"
with tempfile.SpooledTemporaryFile(mode=mode) as handle:
    handle.write(content)
    handle.seek(0)
    df = parser.read_csv(handle)
expected = DataFrame([], columns=["abcd"])
tm.assert_frame_equal(df, expected)
