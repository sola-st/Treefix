# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_round.py
# See GH#14197
df = Series([1.53, np.nan, 0.06]).to_frame()
with tm.assert_produces_warning(None):
    result = df.round()
expected = Series([2.0, np.nan, 0.0]).to_frame()
tm.assert_frame_equal(result, expected)
