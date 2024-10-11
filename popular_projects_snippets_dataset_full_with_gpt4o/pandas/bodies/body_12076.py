# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_comment.py
parser = all_parsers
data = """A,B,C
1,2.,4.#hello world
5.,NaN,10.0
"""
expected = DataFrame(
    [[1.0, 2.0, 4.0], [5.0, np.nan, 10.0]], columns=["A", "B", "C"]
)
result = parser.read_csv(StringIO(data), comment="#", na_values=na_values)
tm.assert_frame_equal(result, expected)
