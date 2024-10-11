# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
piece = float_frame.loc[float_frame.index[:2], ["A", "B"]]
piece.index = float_frame.index[-2:]
piece.columns = ["A", "B"]
float_frame.loc[float_frame.index[-2:], ["A", "B"]] = piece
result = float_frame.loc[float_frame.index[-2:], ["A", "B"]].values
expected = piece.values
tm.assert_almost_equal(result, expected)
