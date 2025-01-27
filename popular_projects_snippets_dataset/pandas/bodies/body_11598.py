# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_mangle_dupes.py
# GH#14704
parser = all_parsers

data = ",Unnamed: 0,,Unnamed: 2\n1,2,3,4"
result = parser.read_csv(StringIO(data))
expected = DataFrame(
    [[1, 2, 3, 4]],
    columns=["Unnamed: 0.1", "Unnamed: 0", "Unnamed: 2.1", "Unnamed: 2"],
)
tm.assert_frame_equal(result, expected)
