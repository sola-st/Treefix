# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_empty.py
result = concat(
    [
        Series(dtype="float64").astype("Sparse"),
        Series(dtype="float64").astype("Sparse"),
    ]
)
assert result.dtype == "Sparse[float64]"

result = concat(
    [Series(dtype="float64").astype("Sparse"), Series(dtype="float64")]
)
expected = pd.SparseDtype(np.float64)
assert result.dtype == expected

result = concat(
    [Series(dtype="float64").astype("Sparse"), Series(dtype="object")]
)
expected = pd.SparseDtype("object")
assert result.dtype == expected
