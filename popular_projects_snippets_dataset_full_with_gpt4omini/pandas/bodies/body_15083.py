# Extracted from ./data/repos/pandas/pandas/tests/base/test_conversion.py
i = CategoricalIndex([Timestamp("1999-12-31"), Timestamp("2000-12-31")])

result = method(i)[0]
assert isinstance(result, Timestamp)
