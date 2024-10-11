# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_empty.py
parser = all_parsers

data = "one,one"
result = parser.read_csv(StringIO(data), dtype={0: "u1", 1: "f"})

expected = DataFrame(
    {"one": np.empty(0, dtype="u1"), "one.1": np.empty(0, dtype="f")},
)
tm.assert_frame_equal(result, expected)
