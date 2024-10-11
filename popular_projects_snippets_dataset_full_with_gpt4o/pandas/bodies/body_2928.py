# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_to_period.py
K = 5

dr = date_range("1/1/2000", "1/1/2001", freq="D")
obj = DataFrame(
    np.random.randn(len(dr), K), index=dr, columns=["A", "B", "C", "D", "E"]
)
obj["mix"] = "a"
obj = tm.get_obj(obj, frame_or_series)

pts = obj.to_period()
exp = obj.copy()
exp.index = period_range("1/1/2000", "1/1/2001")
tm.assert_equal(pts, exp)

pts = obj.to_period("M")
exp.index = exp.index.asfreq("M")
tm.assert_equal(pts, exp)
