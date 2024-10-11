# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
df = frame_of_index_cols
df.index.name = index_name

keys = [box1(df["A"]), box2(df["A"])]
result = df.set_index(keys, drop=drop, append=append)

# if either box is iter, it has been consumed; re-read
keys = [box1(df["A"]), box2(df["A"])]

# need to adapt first drop for case that both keys are 'A' --
# cannot drop the same column twice;
# plain == would give ambiguous Boolean error for containers
first_drop = (
    False
    if (
        isinstance(keys[0], str)
        and keys[0] == "A"
        and isinstance(keys[1], str)
        and keys[1] == "A"
    )
    else drop
)
# to test against already-tested behaviour, we add sequentially,
# hence second append always True; must wrap keys in list, otherwise
# box = list would be interpreted as keys
expected = df.set_index([keys[0]], drop=first_drop, append=append)
expected = expected.set_index([keys[1]], drop=drop, append=True)
tm.assert_frame_equal(result, expected)
