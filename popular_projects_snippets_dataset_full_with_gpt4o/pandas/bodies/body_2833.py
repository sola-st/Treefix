# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reindex.py
df = DataFrame(
    {
        "A": np.arange(3, dtype="int64"),
    },
    index=CategoricalIndex(list("abc"), dtype=CDT(list("cabe")), name="B"),
)

# reindexing
# convert to a regular index
result = df.reindex(["a", "b", "e"])
expected = DataFrame({"A": [0, 1, np.nan], "B": Series(list("abe"))}).set_index(
    "B"
)
tm.assert_frame_equal(result, expected, check_index_type=True)

result = df.reindex(["a", "b"])
expected = DataFrame({"A": [0, 1], "B": Series(list("ab"))}).set_index("B")
tm.assert_frame_equal(result, expected, check_index_type=True)

result = df.reindex(["e"])
expected = DataFrame({"A": [np.nan], "B": Series(["e"])}).set_index("B")
tm.assert_frame_equal(result, expected, check_index_type=True)

result = df.reindex(["d"])
expected = DataFrame({"A": [np.nan], "B": Series(["d"])}).set_index("B")
tm.assert_frame_equal(result, expected, check_index_type=True)

# since we are actually reindexing with a Categorical
# then return a Categorical
cats = list("cabe")

result = df.reindex(Categorical(["a", "e"], categories=cats))
expected = DataFrame(
    {"A": [0, np.nan], "B": Series(list("ae")).astype(CDT(cats))}
).set_index("B")
tm.assert_frame_equal(result, expected, check_index_type=True)

result = df.reindex(Categorical(["a"], categories=cats))
expected = DataFrame(
    {"A": [0], "B": Series(list("a")).astype(CDT(cats))}
).set_index("B")
tm.assert_frame_equal(result, expected, check_index_type=True)

result = df.reindex(["a", "b", "e"])
expected = DataFrame({"A": [0, 1, np.nan], "B": Series(list("abe"))}).set_index(
    "B"
)
tm.assert_frame_equal(result, expected, check_index_type=True)

result = df.reindex(["a", "b"])
expected = DataFrame({"A": [0, 1], "B": Series(list("ab"))}).set_index("B")
tm.assert_frame_equal(result, expected, check_index_type=True)

result = df.reindex(["e"])
expected = DataFrame({"A": [np.nan], "B": Series(["e"])}).set_index("B")
tm.assert_frame_equal(result, expected, check_index_type=True)

# give back the type of categorical that we received
result = df.reindex(Categorical(["a", "e"], categories=cats, ordered=True))
expected = DataFrame(
    {"A": [0, np.nan], "B": Series(list("ae")).astype(CDT(cats, ordered=True))}
).set_index("B")
tm.assert_frame_equal(result, expected, check_index_type=True)

result = df.reindex(Categorical(["a", "d"], categories=["a", "d"]))
expected = DataFrame(
    {"A": [0, np.nan], "B": Series(list("ad")).astype(CDT(["a", "d"]))}
).set_index("B")
tm.assert_frame_equal(result, expected, check_index_type=True)

df2 = DataFrame(
    {
        "A": np.arange(6, dtype="int64"),
    },
    index=CategoricalIndex(list("aabbca"), dtype=CDT(list("cabe")), name="B"),
)
# passed duplicate indexers are not allowed
msg = "cannot reindex on an axis with duplicate labels"
with pytest.raises(ValueError, match=msg):
    df2.reindex(["a", "b"])

# args NotImplemented ATM
msg = r"argument {} is not implemented for CategoricalIndex\.reindex"
with pytest.raises(NotImplementedError, match=msg.format("method")):
    df.reindex(["a"], method="ffill")
with pytest.raises(NotImplementedError, match=msg.format("level")):
    df.reindex(["a"], level=1)
with pytest.raises(NotImplementedError, match=msg.format("limit")):
    df.reindex(["a"], limit=2)
