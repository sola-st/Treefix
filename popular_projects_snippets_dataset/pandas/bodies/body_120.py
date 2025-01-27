# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
# GH#36785
expected = DataFrame({"A": [Timestamp("2013-01-01", tz="UTC")]})
result = expected.apply(lambda x: x, axis=1)
tm.assert_frame_equal(result, expected)
