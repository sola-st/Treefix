# Extracted from ./data/repos/pandas/pandas/tests/frame/test_nonunique_indexes.py
# mixed column selection
# GH 5639
dfbool = DataFrame(
    {
        "one": Series([True, True, False], index=["a", "b", "c"]),
        "two": Series([False, False, True, False], index=["a", "b", "c", "d"]),
        "three": Series([False, True, True, True], index=["a", "b", "c", "d"]),
    }
)
expected = pd.concat([dfbool["one"], dfbool["three"], dfbool["one"]], axis=1)
result = dfbool[["one", "three", "one"]]
check(result, expected)
