# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 9186 & GH 13483 & GH 49240
df = DataFrame(
    {
        "A": [2, 2, 3, 3, 2],
        "id": [5, 6, 7, 8, 9],
        "C": ["p", "q", "q", "p", "q"],
        "D": [None, None, None, None, None],
    }
)
result = df.pivot_table(
    index="A", columns="D", values="id", aggfunc=np.size, margins=margins
)
exp_cols = Index([], name="D")
expected = DataFrame(index=Index([], dtype="int64", name="A"), columns=exp_cols)
tm.assert_frame_equal(result, expected)
