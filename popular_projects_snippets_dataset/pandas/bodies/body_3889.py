# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
columns = MultiIndex.from_tuples(list(itertools.product(range(3), repeat=3)))
df = DataFrame(np.random.randn(30, 27), columns=columns)

tm.assert_frame_equal(df.stack(level=[1, 2]), df.stack(level=1).stack(level=1))
tm.assert_frame_equal(
    df.stack(level=[-2, -1]), df.stack(level=1).stack(level=1)
)

df_named = df.copy()
return_value = df_named.columns.set_names(range(3), inplace=True)
assert return_value is None

tm.assert_frame_equal(
    df_named.stack(level=[1, 2]), df_named.stack(level=1).stack(level=1)
)
