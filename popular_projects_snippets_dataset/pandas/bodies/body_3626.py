# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_drop.py
df = DataFrame(
    [[1, 2, 3], [3, 4, 5], [5, 6, 7]],
    index=["a", "b", "c"],
    columns=["d", "e", "f"],
)
df.index.name, df.columns.name = "first", "second"
df_dropped_b = df.drop("b")
df_dropped_e = df.drop("e", axis=1)
df_inplace_b, df_inplace_e = df.copy(), df.copy()
return_value = df_inplace_b.drop("b", inplace=True)
assert return_value is None
return_value = df_inplace_e.drop("e", axis=1, inplace=True)
assert return_value is None
for obj in (df_dropped_b, df_dropped_e, df_inplace_b, df_inplace_e):
    assert obj.index.name == "first"
    assert obj.columns.name == "second"
assert list(df.columns) == ["d", "e", "f"]

msg = r"\['g'\] not found in axis"
with pytest.raises(KeyError, match=msg):
    df.drop(["g"])
with pytest.raises(KeyError, match=msg):
    df.drop(["g"], axis=1)

# errors = 'ignore'
dropped = df.drop(["g"], errors="ignore")
expected = Index(["a", "b", "c"], name="first")
tm.assert_index_equal(dropped.index, expected)

dropped = df.drop(["b", "g"], errors="ignore")
expected = Index(["a", "c"], name="first")
tm.assert_index_equal(dropped.index, expected)

dropped = df.drop(["g"], axis=1, errors="ignore")
expected = Index(["d", "e", "f"], name="second")
tm.assert_index_equal(dropped.columns, expected)

dropped = df.drop(["d", "g"], axis=1, errors="ignore")
expected = Index(["e", "f"], name="second")
tm.assert_index_equal(dropped.columns, expected)

# GH 16398
dropped = df.drop([], errors="ignore")
expected = Index(["a", "b", "c"], name="first")
tm.assert_index_equal(dropped.index, expected)
