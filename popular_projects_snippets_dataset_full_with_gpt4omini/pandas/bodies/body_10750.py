# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_function.py
# GH 17015
source_dict = {
    "A": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"],
    "B": ["a", "a", "a", "b", "b", "b", "c", "c", "c", "d", "d"],
    "C": in_vals,
}
df = DataFrame(source_dict)
result = df.groupby("B").C.is_monotonic_increasing
index = Index(list("abcd"), name="B")
expected = Series(index=index, data=out_vals, name="C")
tm.assert_series_equal(result, expected)

# Also check result equal to manually taking x.is_monotonic_increasing.
expected = df.groupby(["B"]).C.apply(lambda x: x.is_monotonic_increasing)
tm.assert_series_equal(result, expected)
