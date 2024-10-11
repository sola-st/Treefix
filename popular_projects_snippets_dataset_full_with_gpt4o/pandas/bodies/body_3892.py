# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
df = DataFrame(
    [False, False],
    index=MultiIndex.from_arrays([["a", "b"], ["c", "l"]]),
    columns=["col"],
)
rs = df.unstack()
xp = DataFrame(
    np.array([[False, np.nan], [np.nan, False]], dtype=object),
    index=["a", "b"],
    columns=MultiIndex.from_arrays([["col", "col"], ["c", "l"]]),
)
tm.assert_frame_equal(rs, xp)
