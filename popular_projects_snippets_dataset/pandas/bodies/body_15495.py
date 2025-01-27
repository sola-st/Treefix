# Extracted from ./data/repos/pandas/pandas/tests/series/test_subclass.py
s = tm.SubclassedSeries([1, 2, 3, 4], index=list("abcd"), name="xxx")
res = s.to_frame()
exp = tm.SubclassedDataFrame({"xxx": [1, 2, 3, 4]}, index=list("abcd"))
tm.assert_frame_equal(res, exp)
