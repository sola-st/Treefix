# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# see gh-18166
nested1 = OrderedDict([("b", 1), ("a", 2)])
nested2 = OrderedDict([("b", 2), ("a", 5)])
data = OrderedDict([("col2", nested1), ("col1", nested2)])
result = DataFrame(data)
data = {"col2": [1, 2], "col1": [2, 5]}
expected = DataFrame(data=data, index=["b", "a"])
tm.assert_frame_equal(result, expected)
