# Extracted from ./data/repos/pandas/pandas/tests/window/test_rolling.py
"""
    Ensure that a symmetrical inverted index return same result as non-inverted.
    """
#  GH 43927

index = date_range("2020", periods=4, freq="1s")
df_inc = frame_or_series(range(4), index=index)
df_dec = frame_or_series(range(4), index=index[::-1])

expected_inc = frame_or_series(expected, index=index)
expected_dec = frame_or_series(expected, index=index[::-1])

result_inc = df_inc.rolling(window, closed=closed, center=True).sum()
result_dec = df_dec.rolling(window, closed=closed, center=True).sum()

tm.assert_equal(result_inc, expected_inc)
tm.assert_equal(result_dec, expected_dec)
