# Extracted from ./data/repos/pandas/pandas/tests/frame/test_api.py
assert len(float_frame) == len(float_frame.index)

# single block corner case
arr = float_frame[["A", "B"]].values
expected = float_frame.reindex(columns=["A", "B"]).values
tm.assert_almost_equal(arr, expected)
