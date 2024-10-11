# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_any_all.py
# 21668
df = DataFrame([[True, True]], columns=["a", "a"])
grp_by = df.groupby([0])
result = getattr(grp_by, bool_agg_func)()

expected = df.set_axis(np.array([0]))
tm.assert_frame_equal(result, expected)
