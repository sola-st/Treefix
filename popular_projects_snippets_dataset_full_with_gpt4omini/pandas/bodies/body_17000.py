# Extracted from ./data/repos/pandas/pandas/tests/reshape/concat/test_series.py
# GH39401
obj = frame_or_series([100])
result = concat([obj.iloc[::-1]])
tm.assert_equal(result, obj)
