# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_categorical.py
parser = all_parsers
dtype = {"b": CategoricalDtype(["a", "b", "d", "e"])}

data = "b\nd\na\nc\nd"  # Unexpected c
expected = DataFrame({"b": Categorical(list("dacd"), dtype=dtype["b"])})

result = parser.read_csv(StringIO(data), dtype=dtype)
tm.assert_frame_equal(result, expected)
