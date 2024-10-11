# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_empty.py

assert (
    concat(
        [Series(dtype="M8[ns]"), Series(dtype=np.bool_), Series(dtype=np.int64)]
    ).dtype
    == np.object_
)
