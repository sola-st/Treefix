# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_replace.py
# GH#34871
obj = DataFrame({"Per": [value] * 3})
obj = tm.get_obj(obj, frame_or_series)

expected = obj.copy()
result = obj.replace(1.0, 0.0)
tm.assert_equal(expected, result)
