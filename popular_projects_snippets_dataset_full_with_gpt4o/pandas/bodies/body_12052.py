# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_c_parser_only.py
# See gh-12494
#
# Cause of error was that the C parser
# was not increasing the buffer size when
# the desired space would fill the buffer
# to capacity, which would later cause a
# buffer overflow error when checking the
# EOF terminator of the CSV stream.
parser = c_parser_only

def test_empty_header_read(count):
    with StringIO("," * count) as s:
        expected = DataFrame(columns=[f"Unnamed: {i}" for i in range(count + 1)])
        df = parser.read_csv(s)
    tm.assert_frame_equal(df, expected)

for cnt in range(1, 101):
    test_empty_header_read(cnt)
