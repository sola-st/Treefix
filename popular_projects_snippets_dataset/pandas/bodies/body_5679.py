# Extracted from ./data/repos/pandas/pandas/tests/test_algos.py
idx = Index([1, 2, 3])
exp = Series([1, 2, 3], dtype=np.int64)
tm.assert_numpy_array_equal(algos.mode(idx), exp.values)

idx = Index([1, "a", "a"])
exp = Series(["a"], dtype=object)
tm.assert_numpy_array_equal(algos.mode(idx), exp.values)

idx = Index([1, 1, 2, 3, 3])
exp = Series([1, 3], dtype=np.int64)
tm.assert_numpy_array_equal(algos.mode(idx), exp.values)

idx = Index(
    ["1 day", "1 day", "-1 day", "-1 day 2 min", "2 min", "2 min"],
    dtype="timedelta64[ns]",
)
with pytest.raises(AttributeError, match="TimedeltaIndex"):
    # algos.mode expects Arraylike, does *not* unwrap TimedeltaIndex
    algos.mode(idx)
