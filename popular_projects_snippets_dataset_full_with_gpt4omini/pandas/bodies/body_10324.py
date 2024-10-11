# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_nth.py
# GH 32800, 38286
result = getattr(df.groupby("id"), method)()
tm.assert_frame_equal(result, expected)
