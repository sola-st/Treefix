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

animal_hair_stacked = df.stack(level=["animal", "hair_length"])
exp_hair_stacked = df.stack(level=["exp", "hair_length"])

# GH #8584: Need to check that stacking works when a number
# is passed that is both a level name and in the range of
# the level numbers
df2 = df.copy()
df2.columns.names = ["exp", "animal", 1]
tm.assert_frame_equal(
    df2.stack(level=["animal", 1]), animal_hair_stacked, check_names=False
)
tm.assert_frame_equal(
    df2.stack(level=["exp", 1]), exp_hair_stacked, check_names=False
)

# When mixed types are passed and the ints are not level
# names, raise
msg = (
    "level should contain all level names or all level numbers, not "
    "a mixture of the two"
)
with pytest.raises(ValueError, match=msg):
    df2.stack(level=["animal", 0])

# GH #8584: Having 0 in the level names could raise a
# strange error about lexsort depth
df3 = df.copy()
df3.columns.names = ["exp", "animal", 0]
tm.assert_frame_equal(
    df3.stack(level=["animal", 0]), animal_hair_stacked, check_names=False
)
