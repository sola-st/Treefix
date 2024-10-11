# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_join.py
key1 = ["bar", "bar", "bar", "foo", "foo", "baz", "baz", "qux", "qux", "snap"]
key2 = [
    "two",
    "one",
    "three",
    "one",
    "two",
    "one",
    "two",
    "two",
    "three",
    "one",
]

data = np.random.randn(len(key1))
data = DataFrame({"key1": key1, "key2": key2, "data": data})

index = lexsorted_two_level_string_multiindex
to_join = DataFrame(
    np.random.randn(10, 3), index=index, columns=["j_one", "j_two", "j_three"]
)

joined = data.join(to_join, on=["key1", "key2"], how="inner")
expected = merge(
    data,
    to_join.reset_index(),
    left_on=["key1", "key2"],
    right_on=["first", "second"],
    how="inner",
    sort=False,
)

expected2 = merge(
    to_join,
    data,
    right_on=["key1", "key2"],
    left_index=True,
    how="inner",
    sort=False,
)
tm.assert_frame_equal(joined, expected2.reindex_like(joined))

expected2 = merge(
    to_join,
    data,
    right_on=["key1", "key2"],
    left_index=True,
    how="inner",
    sort=False,
)

expected = expected.drop(["first", "second"], axis=1)
expected.index = joined.index

assert joined.index.is_monotonic_increasing
tm.assert_frame_equal(joined, expected)
