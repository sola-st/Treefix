# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_infer_objects.py
# GH#50090
ii = interval_range(1, 10)
obj = index_or_series(ii)

result = obj.astype(object).infer_objects()
tm.assert_equal(result, obj)
