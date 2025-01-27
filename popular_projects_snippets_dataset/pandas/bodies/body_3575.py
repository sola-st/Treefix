# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sort_index.py

np.random.seed(0)
data = np.random.randn(3, 4)

columns = MultiIndex.from_tuples([("red", i) for i in gen])
df = DataFrame(data, index=list("def"), columns=columns)
df2 = pd.concat(
    [
        df,
        DataFrame(
            "world",
            index=list("def"),
            columns=MultiIndex.from_tuples([("red", extra)]),
        ),
    ],
    axis=1,
)

# check that the repr is good
# make sure that we have a correct sparsified repr
# e.g. only 1 header of read
assert str(df2).splitlines()[0].split() == ["red"]

# GH 8017
# sorting fails after columns added

# construct single-dtype then sort
result = df.copy().sort_index(axis=1)
expected = df.iloc[:, [0, 2, 1, 3]]
tm.assert_frame_equal(result, expected)

result = df2.sort_index(axis=1)
expected = df2.iloc[:, [0, 2, 1, 4, 3]]
tm.assert_frame_equal(result, expected)

# setitem then sort
result = df.copy()
result[("red", extra)] = "world"

result = result.sort_index(axis=1)
tm.assert_frame_equal(result, expected)
