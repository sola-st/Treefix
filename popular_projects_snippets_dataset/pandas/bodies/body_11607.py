# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_empty.py
parser = all_parsers

data = "one,two"
result = parser.read_csv(
    StringIO(data), index_col=["one"], dtype={"one": "u1", 1: "f"}
)

expected = DataFrame(
    {"two": np.empty(0, dtype="f")}, index=Index([], dtype="u1", name="one")
)
tm.assert_frame_equal(result, expected)
