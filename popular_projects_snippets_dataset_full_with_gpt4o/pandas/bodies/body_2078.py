# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# we should get an OutOfBoundsDatetime, NOT OverflowError
# TODO: Timestamp raises VaueError("could not convert string to Timestamp")
#  can we make these more consistent?
arg = "08335394550"
msg = 'Parsing "08335394550" to datetime overflows, at position 0'
with pytest.raises(OutOfBoundsDatetime, match=msg):
    to_datetime(arg)

with pytest.raises(OutOfBoundsDatetime, match=msg):
    to_datetime([arg])

res = to_datetime(arg, errors="coerce")
assert res is NaT
res = to_datetime([arg], errors="coerce")
tm.assert_index_equal(res, Index([NaT]))

res = to_datetime(arg, errors="ignore")
assert isinstance(res, str) and res == arg
res = to_datetime([arg], errors="ignore")
tm.assert_index_equal(res, Index([arg], dtype=object))
