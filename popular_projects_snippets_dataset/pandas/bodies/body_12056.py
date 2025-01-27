# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_c_parser_only.py
# see gh-15140
parser = c_parser_only
df = parser.read_csv(StringIO("a"), header=None, float_precision="round_trip")
tm.assert_frame_equal(df, DataFrame({0: ["a"]}))
