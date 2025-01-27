# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby_dropna.py
# GH 3729
df_list = [
    ["B", 12, 12, 12],
    [None, 12.3, 233.0, 12],
    ["A", 123.23, 123, 1],
    ["B", 1, 1, 1.0],
]
df = pd.DataFrame(df_list, columns=["a", "b", "c", "d"])
grouped = df.groupby("a", dropna=dropna).sum()

expected = pd.DataFrame(outputs, index=pd.Index(idx, dtype="object", name="a"))

tm.assert_frame_equal(grouped, expected)
