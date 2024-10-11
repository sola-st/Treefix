# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# the first dict element sets the ordering for the DataFrame,
# even if there are conflicting orders from subsequent ones
row_one = dict_type()
row_one["b"] = 2
row_one["a"] = 1

row_two = dict_type()
row_two["a"] = 1
row_two["b"] = 2

row_three = {"b": 2, "a": 1}

expected = DataFrame([[2, 1], [2, 1]], columns=["b", "a"])
result = DataFrame([row_one, row_two])
tm.assert_frame_equal(result, expected)

expected = DataFrame([[2, 1], [2, 1], [2, 1]], columns=["b", "a"])
result = DataFrame([row_one, row_two, row_three])
tm.assert_frame_equal(result, expected)
