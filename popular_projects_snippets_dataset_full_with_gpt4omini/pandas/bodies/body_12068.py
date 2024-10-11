# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_c_parser_only.py
# GH 11020
parser = c_parser_only
with tm.ensure_clean() as path:
    with open(path, "w", newline="\n") as f:
        f.write("blah\n\ncol_1,col_2,col_3\n\n")
    result = parser.read_csv(path, skiprows=2, encoding="utf-8", engine="c")
expected = DataFrame(columns=["col_1", "col_2", "col_3"])
tm.assert_frame_equal(result, expected)
