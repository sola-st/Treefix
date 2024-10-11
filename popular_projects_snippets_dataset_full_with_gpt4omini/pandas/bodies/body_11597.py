# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_mangle_dupes.py
# GH#14704
parser = all_parsers

data = "a,a,a.1,a,a.3,a.1,a.1.1\n1,2,3,4,5,6,7"
result = parser.read_csv(StringIO(data))
expected = DataFrame(
    [[1, 2, 3, 4, 5, 6, 7]],
    columns=["a", "a.2", "a.1", "a.4", "a.3", "a.1.2", "a.1.1"],
)
tm.assert_frame_equal(result, expected)
