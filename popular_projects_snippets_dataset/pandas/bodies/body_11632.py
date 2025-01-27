# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_dtypes_basic.py
parser = all_parsers
data = """\
one,two
1,2.5
2,3.5
3,4.5
4,5.5"""
expected = DataFrame(
    [[1, "2.5"], [2, "3.5"], [3, "4.5"], [4, "5.5"]], columns=["one", "two"]
)
expected["one"] = expected["one"].astype(np.float64)
expected["two"] = expected["two"].astype(object)

result = parser.read_csv(StringIO(data), dtype={"one": np.float64, 1: str})
tm.assert_frame_equal(result, expected)
