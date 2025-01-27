# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
# https://github.com/pandas-dev/pandas/issues/32395
df = expected = pd.DataFrame({"data": pd.Series(data)})
result = pd.DataFrame(index=df.index)

key = full_indexer(df)
result.loc[key, "data"] = df["data"]

self.assert_frame_equal(result, expected)
