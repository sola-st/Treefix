# Extracted from ./data/repos/pandas/pandas/tests/extension/base/dim2.py
arr2d = data.repeat(2).reshape(-1, 2)

df = pd.DataFrame(arr2d)
expected = pd.DataFrame({0: arr2d[:, 0], 1: arr2d[:, 1]})
self.assert_frame_equal(df, expected)
