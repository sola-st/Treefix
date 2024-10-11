# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_fillna.py
# GH#45603 preserve object dtype with downcast=False
obj = frame_or_series([1, 2, 3], dtype="object")
result = obj.fillna("", downcast=False)
tm.assert_equal(result, obj)
