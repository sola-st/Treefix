# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_common_basic.py
# GH 28071
ref = DataFrame(
    [[np.nan, np.nan], [np.nan, np.nan], [1, 2], [np.nan, np.nan], [3, 4]],
    columns=list("ab"),
)
csv = "\nheader\n\na,b\n\n\n1,2\n\n3,4"
parser = all_parsers
df = parser.read_csv(StringIO(csv), header=3, nrows=nrows, skip_blank_lines=False)
tm.assert_frame_equal(df, ref[:nrows])
