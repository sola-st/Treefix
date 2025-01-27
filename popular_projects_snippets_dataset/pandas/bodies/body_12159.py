# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_skiprows.py
# see gh-4382
parser = all_parsers
data = "a,b,c\n" + "\n".join(
    [",".join([str(i), str(i + 1), str(i + 2)]) for i in range(10)]
)
condensed_data = "a,b,c\n" + "\n".join(
    [",".join([str(i), str(i + 1), str(i + 2)]) for i in [0, 1, 2, 3, 4, 6, 8, 9]]
)

result = parser.read_csv(StringIO(data), skiprows=[6, 8])
condensed_result = parser.read_csv(StringIO(condensed_data))
tm.assert_frame_equal(result, condensed_result)
