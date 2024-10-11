# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_pipe.py
obj = DataFrame({"A": [1, 2, 3]})
obj = tm.get_obj(obj, frame_or_series)

f = lambda x, y: y
result = obj.pipe((f, "y"), 0)
tm.assert_equal(result, obj)
