# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_multi.py

on_cols = ["k1", "k2"]
left = DataFrame(
    {
        "k1": [0, 1, 2] * 8,
        "k2": ["foo", "bar"] * 12,
        "v": np.array(np.arange(24), dtype=np.int64),
    }
)

index = MultiIndex.from_tuples([(2, "bar"), (1, "foo")])
right = DataFrame({"v2": [5, 7]}, index=index)

result = left.join(right, on=on_cols)

expected = left.copy()
expected["v2"] = np.nan
expected.loc[(expected.k1 == 2) & (expected.k2 == "bar"), "v2"] = 5
expected.loc[(expected.k1 == 1) & (expected.k2 == "foo"), "v2"] = 7

tm.assert_frame_equal(result, expected)

result.sort_values(on_cols, kind="mergesort", inplace=True)
expected = left.join(right, on=on_cols, sort=True)

tm.assert_frame_equal(result, expected)

# test join with multi dtypes blocks
left = DataFrame(
    {
        "k1": [0, 1, 2] * 8,
        "k2": ["foo", "bar"] * 12,
        "k3": np.array([0, 1, 2] * 8, dtype=np.float32),
        "v": np.array(np.arange(24), dtype=np.int32),
    }
)

index = MultiIndex.from_tuples([(2, "bar"), (1, "foo")])
right = DataFrame({"v2": [5, 7]}, index=index)

result = left.join(right, on=on_cols)

expected = left.copy()
expected["v2"] = np.nan
expected.loc[(expected.k1 == 2) & (expected.k2 == "bar"), "v2"] = 5
expected.loc[(expected.k1 == 1) & (expected.k2 == "foo"), "v2"] = 7

tm.assert_frame_equal(result, expected)

result = result.sort_values(on_cols, kind="mergesort")
expected = left.join(right, on=on_cols, sort=True)

tm.assert_frame_equal(result, expected)
