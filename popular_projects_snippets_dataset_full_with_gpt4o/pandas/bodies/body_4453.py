# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# see gh-13304
expected = DataFrame([[2, 1]], columns=["b", "a"])

data = dict_type()
data["b"] = [2]
data["a"] = [1]

result = DataFrame(data)
tm.assert_frame_equal(result, expected)

data = dict_type()
data["b"] = 2
data["a"] = 1

result = DataFrame([data])
tm.assert_frame_equal(result, expected)
