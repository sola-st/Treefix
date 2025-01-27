# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py
tuples = [(1, 2, 3), (1, 2, 3), (2, 5, 3)]

columns = ["a", "b", "c"]
original_columns = list(columns)

df = DataFrame.from_records(tuples, columns=columns, index="a")  # noqa

assert columns == original_columns
