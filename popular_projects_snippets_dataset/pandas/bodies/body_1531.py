# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
idx = key_type(["A", "B", "C"])
result = float_frame.loc[:, idx]
expected = float_frame.loc[:, ["A", "B", "C"]]
tm.assert_frame_equal(result, expected)
