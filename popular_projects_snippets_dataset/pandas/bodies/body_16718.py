# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py

dtype1 = np.dtype(d1)
dtype2 = np.dtype(d2)

left = DataFrame(
    {
        "k1": np.array([0, 1, 2] * 8, dtype=dtype1),
        "k2": ["foo", "bar"] * 12,
        "v": np.array(np.arange(24), dtype=np.int64),
    }
)

index = MultiIndex.from_tuples([(2, "bar"), (1, "foo")])
right = DataFrame({"v2": np.array([5, 7], dtype=dtype2)}, index=index)

result = left.join(right, on=["k1", "k2"])

expected = left.copy()

if dtype2.kind == "i":
    dtype2 = np.dtype("float64")
expected["v2"] = np.array(np.nan, dtype=dtype2)
expected.loc[(expected.k1 == 2) & (expected.k2 == "bar"), "v2"] = 5
expected.loc[(expected.k1 == 1) & (expected.k2 == "foo"), "v2"] = 7

tm.assert_frame_equal(result, expected)

result = left.join(right, on=["k1", "k2"], sort=True)
expected.sort_values(["k1", "k2"], kind="mergesort", inplace=True)
tm.assert_frame_equal(result, expected)
