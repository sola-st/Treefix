# Extracted from ./data/repos/pandas/pandas/tests/reshape/merge/test_merge.py
# GH 36973
pcat = CategoricalDtype(categories=["P2", "P1"], ordered=ordered)
df1 = DataFrame(
    {
        "id": ["C", "C", "D"],
        "p": Categorical(["P2", "P1", "P2"], dtype=pcat),
        "a": [0, 1, 2],
    }
).set_index(["id", "p"])
df2 = DataFrame(
    {
        "id": ["A", "C", "C"],
        "p": Categorical(["P2", "P2", "P1"], dtype=pcat),
        "d1": [10, 11, 12],
    }
).set_index(["id", "p"])
result = merge(df1, df2, how="left", left_index=True, right_index=True)
expected = DataFrame(
    {
        "id": ["C", "C", "D"],
        "p": Categorical(["P2", "P1", "P2"], dtype=pcat),
        "a": [0, 1, 2],
        "d1": [11.0, 12.0, np.nan],
    }
).set_index(["id", "p"])
tm.assert_frame_equal(result, expected)
