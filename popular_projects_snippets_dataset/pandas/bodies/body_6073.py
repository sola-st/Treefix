# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
# GH#32959 null slice along index, slice along columns with single-block
df = pd.DataFrame({"A": data})

result = df.iloc[:, :]
self.assert_frame_equal(result, df)

result = df.iloc[:, :1]
self.assert_frame_equal(result, df)

result = df.iloc[:, :2]
self.assert_frame_equal(result, df)

result = df.iloc[:, ::2]
self.assert_frame_equal(result, df)

result = df.iloc[:, 1:2]
self.assert_frame_equal(result, df.iloc[:, :0])

result = df.iloc[:, -1:]
self.assert_frame_equal(result, df)
