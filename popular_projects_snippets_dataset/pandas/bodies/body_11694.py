# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_converters.py
# see gh-1835 , GH#40589
parser = all_parsers
data = "A;B\n1;2\n3;4"

rs = parser.read_csv(
    StringIO(data), sep=";", index_col="A", converters={"A": conv_f}
)

xp = DataFrame({"B": [2, 4]}, index=Index(["1", "3"], name="A", dtype="object"))
tm.assert_frame_equal(rs, xp)
