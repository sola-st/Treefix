# Extracted from ./data/repos/pandas/pandas/tests/series/test_subclass.py
# GH 15564
s = tm.SubclassedSeries([1, 2, 3, 4], index=[list("aabb"), list("xyxy")])

res = s.unstack()
exp = tm.SubclassedDataFrame({"x": [1, 3], "y": [2, 4]}, index=["a", "b"])

tm.assert_frame_equal(res, exp)
