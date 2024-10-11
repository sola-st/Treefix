# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
class CustomDict(dict):
    pass

d = {"a": 1.5, "b": 3}

data_custom = [CustomDict(d)]
data = [d]

result_custom = DataFrame(data_custom)
result = DataFrame(data)
tm.assert_frame_equal(result, result_custom)
