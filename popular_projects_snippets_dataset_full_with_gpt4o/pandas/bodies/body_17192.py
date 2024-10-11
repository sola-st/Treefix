# Extracted from ./data/repos/pandas/pandas/tests/reshape/test_pivot.py
# GH 22159
df = DataFrame(
    {"A": ["one", "two", "one"], "x": [3, np.nan, 2], "y": [1, np.nan, np.nan]}
)

result = pivot_table(df, columns="A", aggfunc=np.mean, dropna=dropna)

data = [[2.5, np.nan], [1, np.nan]]
col = Index(["one", "two"], name="A")
expected = DataFrame(data, index=["x", "y"], columns=col)

if dropna:
    expected = expected.dropna(axis="columns")

tm.assert_frame_equal(result, expected)
