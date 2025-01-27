# Extracted from ./data/repos/pandas/pandas/tests/indexes/interval/test_constructors.py
# mismatched closed within intervals with no constructor override
ivs = [Interval(0, 1, closed="right"), Interval(2, 3, closed="left")]
msg = "intervals must all be closed on the same side"
with pytest.raises(ValueError, match=msg):
    klass(ivs)

# scalar
msg = (
    r"(IntervalIndex|Index)\(...\) must be called with a collection of "
    "some kind, 5 was passed"
)
with pytest.raises(TypeError, match=msg):
    klass(5)

# not an interval; dtype depends on 32bit/windows builds
msg = "type <class 'numpy.int(32|64)'> with value 0 is not an interval"
with pytest.raises(TypeError, match=msg):
    klass([0, 1])
