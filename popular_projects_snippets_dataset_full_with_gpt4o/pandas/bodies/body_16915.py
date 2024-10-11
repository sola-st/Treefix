# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_dataframe.py
t1 = DataFrame(
    {"value": Series([1, 2, 3], index=Index(["a", "b", "c"], name="id"))}
)
t2 = DataFrame({"value": Series([7, 8], index=Index(["a", "b"], name="id"))})

# it works
result = concat([t1, t2], axis=1, keys=["t1", "t2"], sort=sort)
assert list(result.columns) == [("t1", "value"), ("t2", "value")]
