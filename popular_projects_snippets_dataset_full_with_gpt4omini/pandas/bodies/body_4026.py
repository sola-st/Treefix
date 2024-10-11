# Extracted from ./data/repos/pandas/pandas/tests/frame/constructors/test_from_records.py
result = DataFrame.from_records([(1, 2, 3), (4, 5, 6)], columns=["a", "b", "a"])

expected = DataFrame([(1, 2, 3), (4, 5, 6)], columns=["a", "b", "a"])

tm.assert_frame_equal(result, expected)
