# Extracted from ./data/repos/pandas/pandas/tests/arrays/sparse/test_astype.py
# GH 49987
df = DataFrame([["a", 0], ["b", 1], ["b", 2]], columns=["A", "B"])
result = df["A"].astype(SparseDtype("category", fill_value="c"))
expected = Series(
    ["a", "b", "b"], name="A", dtype=SparseDtype("object", fill_value="c")
)
tm.assert_series_equal(result, expected)
