# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH#25797
df = pd.DataFrame.from_dict({"Test": ["0.5", True, "0.6"]})
df["Test"] = df["Test"].replace([True], [np.nan])
expected = pd.DataFrame.from_dict({"Test": ["0.5", np.nan, "0.6"]})
tm.assert_frame_equal(df, expected)

df = pd.DataFrame.from_dict({"Test": ["0.5", None, "0.6"]})
df["Test"] = df["Test"].replace([None], [np.nan])
tm.assert_frame_equal(df, expected)

df = pd.DataFrame.from_dict({"Test": ["0.5", None, "0.6"]})
df["Test"] = df["Test"].fillna(np.nan)
tm.assert_frame_equal(df, expected)
