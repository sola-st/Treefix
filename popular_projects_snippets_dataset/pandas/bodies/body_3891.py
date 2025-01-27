# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
columns = MultiIndex.from_tuples(
    [
        ("A", "cat", "long"),
        ("B", "cat", "long"),
        ("A", "dog", "short"),
        ("B", "dog", "short"),
    ],
    names=["exp", "animal", "hair_length"],
)
df = DataFrame(np.random.randn(4, 4), columns=columns)

exp_animal_stacked = df.stack(level=["exp", "animal"])
animal_hair_stacked = df.stack(level=["animal", "hair_length"])
exp_hair_stacked = df.stack(level=["exp", "hair_length"])

df2 = df.copy()
df2.columns.names = [0, 1, 2]
tm.assert_frame_equal(
    df2.stack(level=[1, 2]), animal_hair_stacked, check_names=False
)
tm.assert_frame_equal(
    df2.stack(level=[0, 1]), exp_animal_stacked, check_names=False
)
tm.assert_frame_equal(
    df2.stack(level=[0, 2]), exp_hair_stacked, check_names=False
)

# Out-of-order int column names
df3 = df.copy()
df3.columns.names = [2, 0, 1]
tm.assert_frame_equal(
    df3.stack(level=[0, 1]), animal_hair_stacked, check_names=False
)
tm.assert_frame_equal(
    df3.stack(level=[2, 0]), exp_animal_stacked, check_names=False
)
tm.assert_frame_equal(
    df3.stack(level=[2, 1]), exp_hair_stacked, check_names=False
)
