# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py
# GH#32503
obj = DataFrame({"col1": range(10, 20), "col2": range(20, 30)})
obj = tm.get_obj(obj, frame_or_series)
result = obj.sample(n=3, random_state=eval(func_str)(arg))
expected = obj.sample(n=3, random_state=com.random_state(eval(func_str)(arg)))
tm.assert_equal(result, expected)
