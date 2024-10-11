# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# GH 4297
# support Array
result = DataFrame({"A": array.array("i", range(10))})
expected = DataFrame({"A": list(range(10))})
tm.assert_frame_equal(result, expected, check_dtype=False)

expected = DataFrame([list(range(10)), list(range(10))])
result = DataFrame([array.array("i", range(10)), array.array("i", range(10))])
tm.assert_frame_equal(result, expected, check_dtype=False)
