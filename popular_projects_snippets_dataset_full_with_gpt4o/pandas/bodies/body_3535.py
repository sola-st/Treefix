# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_index.py
# GH#13743, GH#13854
df = DataFrame(
    {
        "A": [1, 2, 1, 1, 2],
        "B": [10, 16, 22, 28, 34],
        "C1": Categorical(list("abaab"), categories=list("bac"), ordered=False),
        "C2": Categorical(list("abaab"), categories=list("bac"), ordered=True),
    }
)
for cols in ["C1", "C2", ["A", "C1"], ["A", "C2"], ["C1", "C2"]]:
    result = df.set_index(cols).reset_index()
    result = result.reindex(columns=df.columns)
    tm.assert_frame_equal(result, df)
