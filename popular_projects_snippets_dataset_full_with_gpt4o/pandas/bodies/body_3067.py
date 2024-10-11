# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_set_axis.py
# GH14636; this tests setting index for both Series and DataFrame
new_index = list("abcd")[: len(obj)]
expected = obj.copy()
expected.index = new_index
result = obj.set_axis(new_index, axis=0)
tm.assert_equal(expected, result)
