# Extracted from ./data/repos/pandas/pandas/tests/io/parser/dtypes/test_categorical.py
parser = all_parsers
dtype = {"b": CategoricalDtype(pd.to_timedelta(["1H", "2H", "3H"]))}

data = "b\n1H\n2H\n3H"
expected = DataFrame({"b": Categorical(dtype["b"].categories)})

result = parser.read_csv(StringIO(data), dtype=dtype)
tm.assert_frame_equal(result, expected)
