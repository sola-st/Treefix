# Extracted from ./data/repos/pandas/pandas/tests/test_take.py
arr = np.array([], dtype=np.int64)
# empty take is ok
result = algos.take(arr, [], allow_fill=allow_fill)
tm.assert_numpy_array_equal(arr, result)

msg = "|".join(
    [
        "cannot do a non-empty take from an empty axes.",
        "indices are out-of-bounds",
    ]
)
with pytest.raises(IndexError, match=msg):
    algos.take(arr, [0], allow_fill=allow_fill)
