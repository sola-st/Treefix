# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_getitem.py
values = np.arange(10.0, 50.0, 2)
index = Index(values)

start, end = values[[5, 15]]

data = np.random.randn(20, 3)
if frame_or_series is not DataFrame:
    data = data[:, 0]

obj = frame_or_series(data, index=index)

result = obj[start:end]
expected = obj.iloc[5:16]
tm.assert_equal(result, expected)

result = obj.loc[start:end]
tm.assert_equal(result, expected)
