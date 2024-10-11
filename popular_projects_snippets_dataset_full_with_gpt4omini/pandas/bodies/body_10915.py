# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_indexing.py
# GH#44924
df = pd.DataFrame(
    {
        "A": [1, 2],
        "B": [3, 3],
        "C": ["G", "G"],
    }
)
result = df.groupby("C")[func(["A", "B", "A"])].mean()
expected = pd.DataFrame(
    [[1.5, 3.0, 1.5]], columns=["A", "B", "A"], index=pd.Index(["G"], name="C")
)
tm.assert_frame_equal(result, expected)
