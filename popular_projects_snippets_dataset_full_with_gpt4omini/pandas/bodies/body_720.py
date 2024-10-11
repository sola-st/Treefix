# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
r = (5, 6)
values = [r]
lib.to_object_array_tuples(values)

# make sure record array works
record = namedtuple("record", "x y")
r = record(5, 6)
values = [r]
lib.to_object_array_tuples(values)
