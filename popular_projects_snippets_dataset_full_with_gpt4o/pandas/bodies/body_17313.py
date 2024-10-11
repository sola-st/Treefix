# Extracted from ./data/repos/pandas/pandas/tests/generic/test_generic.py
# GH11382

# small
shape = [2000] + ([1] * (frame_or_series._AXIS_LEN - 1))
small = construct(frame_or_series, shape, dtype="int8", value=1)
tm.assert_equal(small.truncate(), small)
tm.assert_equal(small.truncate(before=0, after=3e3), small)
tm.assert_equal(small.truncate(before=-1, after=2e3), small)

# big
shape = [2_000_000] + ([1] * (frame_or_series._AXIS_LEN - 1))
big = construct(frame_or_series, shape, dtype="int8", value=1)
tm.assert_equal(big.truncate(), big)
tm.assert_equal(big.truncate(before=0, after=3e6), big)
tm.assert_equal(big.truncate(before=-1, after=2e6), big)
