# Extracted from ./data/repos/pandas/pandas/tests/extension/base/setitem.py
df = pd.DataFrame({"data": data[:1]})

df.loc[1, "data"] = data[1]
expected = pd.DataFrame({"data": data[:2]})
self.assert_frame_equal(df, expected)

# https://github.com/pandas-dev/pandas/issues/47284
df.loc[2, "data"] = na_value
expected = pd.DataFrame(
    {"data": pd.Series([data[0], data[1], na_value], dtype=data.dtype)}
)
self.assert_frame_equal(df, expected)
