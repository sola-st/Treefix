# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_rename.py
# see gh-23859
colAData = range(1, 11)
colBdata = np.random.randn(10)

df = DataFrame({"A": colAData, "B": colBdata})
result = df.rename(*args, **kwargs)

expected = DataFrame({"a": colAData, "b": colBdata})
tm.assert_frame_equal(result, expected)
