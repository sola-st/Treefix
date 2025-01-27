# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH11181
named_tuple = namedtuple("Pandas", list("ab"))
tuples = [named_tuple(1, 3), named_tuple(2, 4)]
expected = DataFrame({"a": [1, 2], "b": [3, 4]})
result = DataFrame(tuples)
tm.assert_frame_equal(result, expected)

# with columns
expected = DataFrame({"y": [1, 2], "z": [3, 4]})
result = DataFrame(tuples, columns=["y", "z"])
tm.assert_frame_equal(result, expected)
