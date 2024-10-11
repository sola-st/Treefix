# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nth.py
# GH 20520
df = DataFrame(
    {
        "group": ["first", "first", "second", "third", "third"],
        "time": 5 * [np.datetime64("NaT")],
        "categories": Series(["a", "b", "c", "a", "b"], dtype="category"),
    }
)
result = df.groupby("group").first()
expected = DataFrame(
    {
        "time": 3 * [np.datetime64("NaT")],
        "categories": Series(["a", "c", "a"]).astype(
            pd.CategoricalDtype(["a", "b", "c"])
        ),
    }
)
expected.index = Index(["first", "second", "third"], name="group")
tm.assert_frame_equal(result, expected)
