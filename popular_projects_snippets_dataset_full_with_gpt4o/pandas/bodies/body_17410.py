# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets_properties.py
assume(not offset.normalize)
# check that the class-specific implementations of is_on_offset match
# the general case definition:
#   (dt + offset) - offset == dt
try:
    compare = (dt + offset) - offset
except (pytz.NonExistentTimeError, pytz.AmbiguousTimeError):
    # When dt + offset does not exist or is DST-ambiguous, assume(False) to
    # indicate to hypothesis that this is not a valid test case
    # DST-ambiguous example (GH41906):
    # dt = datetime.datetime(1900, 1, 1, tzinfo=pytz.timezone('Africa/Kinshasa'))
    # offset = MonthBegin(66)
    assume(False)

assert offset.is_on_offset(dt) == (compare == dt)
