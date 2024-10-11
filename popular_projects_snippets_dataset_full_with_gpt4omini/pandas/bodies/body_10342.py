# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nth.py
# GH 22512
df = DataFrame(
    {
        "A": [1, 1, 1, 2, 2],
        "B": [100, 100, 200, 100, 100],
        "C": ["apple", "orange", "mango", "mango", "orange"],
        "D": ["jupiter", "mercury", "mars", "venus", "venus"],
    }
)
df = df.astype({"D": "category"})
result = df.groupby(by=["A", "B"]).first()
expected = DataFrame(
    {
        "C": ["apple", "mango", "mango"],
        "D": Series(["jupiter", "mars", "venus"]).astype(
            pd.CategoricalDtype(["jupiter", "mars", "mercury", "venus"])
        ),
    }
)
expected.index = MultiIndex.from_tuples(
    [(1, 100), (1, 200), (2, 100)], names=["A", "B"]
)
tm.assert_frame_equal(result, expected)
