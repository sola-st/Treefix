# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_c_parser_only.py
with StringIO("," * count) as s:
    expected = DataFrame(columns=[f"Unnamed: {i}" for i in range(count + 1)])
    df = parser.read_csv(s)
tm.assert_frame_equal(df, expected)
