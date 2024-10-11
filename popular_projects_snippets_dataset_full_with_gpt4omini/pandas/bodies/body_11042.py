# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_apply.py
# GH #34656
# GH #34271
df = DataFrame(
    {
        "a": [99, 99, 99, 88, 88, 88],
        "b": [1, 2, 3, 4, 5, 6],
        "c": [10, 20, 30, 40, 50, 60],
    }
)

expected = DataFrame(
    {"a": [264, 297], "b": [15, 6], "c": [150, 60]},
    index=Index([88, 99], name="a"),
)

# Check output when no other methods are called before .apply()
grp = df.groupby(by="a")
result = grp.apply(sum)
tm.assert_frame_equal(result, expected)

# Check output when another method is called before .apply()
grp = df.groupby(by="a")
args = get_groupby_method_args(reduction_func, df)
_ = getattr(grp, reduction_func)(*args)
result = grp.apply(sum)
tm.assert_frame_equal(result, expected)
