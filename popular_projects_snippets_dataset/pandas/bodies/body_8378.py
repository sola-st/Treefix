# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH#24255
# check that overflows in calculating `addend = periods * stride`
#  are caught
with tm.assert_produces_warning(None):
    # we should _not_ be seeing a overflow RuntimeWarning
    dti = date_range(start="1677-09-22", periods=213503, freq="D")

assert dti[0] == Timestamp("1677-09-22")
assert len(dti) == 213503

msg = "Cannot generate range with"
with pytest.raises(OutOfBoundsDatetime, match=msg):
    date_range("1969-05-04", periods=200000000, freq="30000D")
