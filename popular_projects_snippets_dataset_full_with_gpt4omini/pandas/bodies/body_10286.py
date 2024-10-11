# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_groupby_dropna.py
# GH#36327
values = np.random.choice([1, 2, None], 30)
df = pd.DataFrame(
    {"x": pd.Categorical(values, categories=[1, 2, 3]), "y": range(len(values))}
)
gb = df.groupby("x", dropna=False)
result = gb.transform(lambda x: x.sum())
expected = gb.transform("sum")
tm.assert_frame_equal(result, expected)
