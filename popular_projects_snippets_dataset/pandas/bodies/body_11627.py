# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_categorical.py
parser = all_parsers
dtype = {"b": CategoricalDtype([Timestamp("2014")])}

data = "b\n2014-01-01\n2014-01-01"
expected = DataFrame({"b": Categorical([Timestamp("2014")] * 2)})

result = parser.read_csv(StringIO(data), dtype=dtype)
tm.assert_frame_equal(result, expected)
