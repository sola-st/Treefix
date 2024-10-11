# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py

left = DataFrame(
    {
        "A": ["foo", "bar"],
        "B": Series(["foo", "bar"]).astype("category"),
        "C": [1, 2],
        "D": [1.0, 2.0],
        "E": Series([1, 2], dtype="uint64"),
        "F": Series([1, 2], dtype="int32"),
    }
)
right = DataFrame({"A": right_vals})

# GH 9780
# We allow merging on object and categorical cols and cast
# categorical cols to object
result = merge(left, right, on="A")
assert is_object_dtype(result.A.dtype)
