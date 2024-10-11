# Extracted from ./data/repos/pandas/pandas/tests/frame/test_nonunique_indexes.py
# insert
df = DataFrame(
    [[1, 1, 1, 5], [1, 1, 2, 5], [2, 1, 3, 5]],
    columns=["foo", "bar", "foo", "hello"],
)
df["string"] = "bah"
expected = DataFrame(
    [[1, 1, 1, 5, "bah"], [1, 1, 2, 5, "bah"], [2, 1, 3, 5, "bah"]],
    columns=["foo", "bar", "foo", "hello", "string"],
)
check(df, expected)
with pytest.raises(ValueError, match="Length of value"):
    df.insert(0, "AnotherColumn", range(len(df.index) - 1))

# insert same dtype
df["foo2"] = 3
expected = DataFrame(
    [[1, 1, 1, 5, "bah", 3], [1, 1, 2, 5, "bah", 3], [2, 1, 3, 5, "bah", 3]],
    columns=["foo", "bar", "foo", "hello", "string", "foo2"],
)
check(df, expected)

# set (non-dup)
df["foo2"] = 4
expected = DataFrame(
    [[1, 1, 1, 5, "bah", 4], [1, 1, 2, 5, "bah", 4], [2, 1, 3, 5, "bah", 4]],
    columns=["foo", "bar", "foo", "hello", "string", "foo2"],
)
check(df, expected)
df["foo2"] = 3

# delete (non dup)
del df["bar"]
expected = DataFrame(
    [[1, 1, 5, "bah", 3], [1, 2, 5, "bah", 3], [2, 3, 5, "bah", 3]],
    columns=["foo", "foo", "hello", "string", "foo2"],
)
check(df, expected)

# try to delete again (its not consolidated)
del df["hello"]
expected = DataFrame(
    [[1, 1, "bah", 3], [1, 2, "bah", 3], [2, 3, "bah", 3]],
    columns=["foo", "foo", "string", "foo2"],
)
check(df, expected)

# consolidate
df = df._consolidate()
expected = DataFrame(
    [[1, 1, "bah", 3], [1, 2, "bah", 3], [2, 3, "bah", 3]],
    columns=["foo", "foo", "string", "foo2"],
)
check(df, expected)

# insert
df.insert(2, "new_col", 5.0)
expected = DataFrame(
    [[1, 1, 5.0, "bah", 3], [1, 2, 5.0, "bah", 3], [2, 3, 5.0, "bah", 3]],
    columns=["foo", "foo", "new_col", "string", "foo2"],
)
check(df, expected)

# insert a dup
with pytest.raises(ValueError, match="cannot insert"):
    df.insert(2, "new_col", 4.0)

df.insert(2, "new_col", 4.0, allow_duplicates=True)
expected = DataFrame(
    [
        [1, 1, 4.0, 5.0, "bah", 3],
        [1, 2, 4.0, 5.0, "bah", 3],
        [2, 3, 4.0, 5.0, "bah", 3],
    ],
    columns=["foo", "foo", "new_col", "new_col", "string", "foo2"],
)
check(df, expected)

# delete (dup)
del df["foo"]
expected = DataFrame(
    [[4.0, 5.0, "bah", 3], [4.0, 5.0, "bah", 3], [4.0, 5.0, "bah", 3]],
    columns=["new_col", "new_col", "string", "foo2"],
)
tm.assert_frame_equal(df, expected)
