# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_c_parser_only.py
parser = c_parser_only
test_input = """\
1 2
2 2 3
3 2 3 # 3 fields
4 2 3# 3 fields
5 2 # 2 fields
6 2# 2 fields
7 # 1 field, NaN
8# 1 field, NaN
9 2 3 # skipped line
# comment"""
df = parser.read_csv(
    StringIO(test_input),
    comment="#",
    header=None,
    delimiter="\\s+",
    skiprows=0,
    on_bad_lines="warn",
)
captured = capsys.readouterr()
# skipped lines 2, 3, 4, 9
for line_num in (2, 3, 4, 9):
    assert f"Skipping line {line_num}" in captured.err
expected = DataFrame([[1, 2], [5, 2], [6, 2], [7, np.nan], [8, np.nan]])
tm.assert_frame_equal(df, expected)
