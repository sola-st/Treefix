# Extracted from ./data/repos/pandas/pandas/tests/arrays/categorical/test_constructors.py
# https://github.com/pandas-dev/pandas/issues/31927
values = klass(["a", nulls_fixture, "b"])
result = Categorical(values)

dtype = CategoricalDtype(["a", "b"])
codes = [0, -1, 1]
expected = Categorical.from_codes(codes=codes, dtype=dtype)

tm.assert_categorical_equal(result, expected)
