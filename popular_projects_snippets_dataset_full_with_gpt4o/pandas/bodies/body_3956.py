# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH# 18265
values = np.arange(5)
data = np.vstack(
    [
        [f"b{x}" for x in values],  # b0, b1, ..
        [f"a{x}" for x in values],  # a0, a1, ..
    ]
)
df = DataFrame(data.T, columns=["b", "a"])
df.columns.name = "first"
second_level_dict = {"x": df}
multi_level_df = pd.concat(second_level_dict, axis=1)
multi_level_df.columns.names = ["second", "first"]
df = multi_level_df.reindex(sorted(multi_level_df.columns), axis=1)
result = df.stack(["first", "second"]).unstack(["first", "second"])
expected = DataFrame(
    [["a0", "b0"], ["a1", "b1"], ["a2", "b2"], ["a3", "b3"], ["a4", "b4"]],
    index=[0, 1, 2, 3, 4],
    columns=MultiIndex.from_tuples(
        [("a", "x"), ("b", "x")], names=["first", "second"]
    ),
)
tm.assert_frame_equal(result, expected)
