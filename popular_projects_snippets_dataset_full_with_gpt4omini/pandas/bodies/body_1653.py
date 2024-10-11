# Extracted from ./data/repos/pandas/pandas/tests/test_sorting.py
# GH9096
values = range(55109)
data = DataFrame.from_dict({"a": values, "b": values, "c": values, "d": values})
grouped = data.groupby(["a", "b", "c", "d"])
assert len(grouped) == len(values)
