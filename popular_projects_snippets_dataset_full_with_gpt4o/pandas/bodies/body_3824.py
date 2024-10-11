# Extracted from ./data/repos/pandas/pandas/tests/frame/test_nonunique_indexes.py
# dup across dtypes
df = DataFrame(
    [[1, 1, 1.0, 5], [1, 1, 2.0, 5], [2, 1, 3.0, 5]],
    columns=["foo", "bar", "foo", "hello"],
)
check(df)

df["foo2"] = 7.0
expected = DataFrame(
    [[1, 1, 1.0, 5, 7.0], [1, 1, 2.0, 5, 7.0], [2, 1, 3.0, 5, 7.0]],
    columns=["foo", "bar", "foo", "hello", "foo2"],
)
check(df, expected)

result = df["foo"]
expected = DataFrame([[1, 1.0], [1, 2.0], [2, 3.0]], columns=["foo", "foo"])
check(result, expected)

# multiple replacements
df["foo"] = "string"
expected = DataFrame(
    [
        ["string", 1, "string", 5, 7.0],
        ["string", 1, "string", 5, 7.0],
        ["string", 1, "string", 5, 7.0],
    ],
    columns=["foo", "bar", "foo", "hello", "foo2"],
)
check(df, expected)

del df["foo"]
expected = DataFrame(
    [[1, 5, 7.0], [1, 5, 7.0], [1, 5, 7.0]], columns=["bar", "hello", "foo2"]
)
check(df, expected)
