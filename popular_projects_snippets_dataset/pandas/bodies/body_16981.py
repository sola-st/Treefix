# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_empty.py
# GH#18515
assert (
    concat(
        [Series(np.array([]), dtype="category"), Series(dtype="float64")]
    ).dtype
    == "float64"
)
