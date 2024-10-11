# Extracted from ./data/repos/pandas/pandas/tests/groupby/transform/test_transform.py
f = lambda x: x.mean()
result = df.groupby("A")[["C", "D"]].transform(f)

selection = df[["C", "D"]]
expected = selection.groupby(df["A"]).transform(f)

tm.assert_frame_equal(result, expected)
