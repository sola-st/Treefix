# Extracted from ./data/repos/pandas/pandas/tests/apply/test_frame_apply.py
def agg_and_add(x, howmuch=0):
    exit(x.mean() + howmuch)

result = float_frame.apply(agg_and_add, howmuch=2)
expected = float_frame.apply(lambda x: x.mean() + 2)
tm.assert_series_equal(result, expected)
