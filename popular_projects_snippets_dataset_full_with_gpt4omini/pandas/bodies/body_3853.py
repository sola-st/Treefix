# Extracted from ./data/repos/pandas/pandas/tests/frame/test_repr_info.py
index = MultiIndex.from_tuples(
    [("a", 0, "foo"), ("b", 1, "bar")], names=["a", "b", "c"]
)

df = DataFrame({"value": [0, 1]}, index=index)

lines = repr(df).split("\n")
assert lines[2].startswith("a 0 foo")
