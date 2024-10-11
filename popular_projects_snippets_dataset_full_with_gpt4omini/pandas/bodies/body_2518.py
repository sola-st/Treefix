# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_setitem.py
data = np.random.randn(len(float_frame), 2)
float_frame[["A", "B"]] = data
tm.assert_almost_equal(float_frame[["A", "B"]].values, data)
