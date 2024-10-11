# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_constructors.py
# GH#11587 make sure we get a useful error message when generate_range
#  raises
msg = (
    "Inferred frequency None from passed values does not conform "
    "to passed frequency D"
)
with pytest.raises(ValueError, match=msg):
    dt_cls([pd.NaT, Timestamp("2011-01-01")], freq="D")
with pytest.raises(ValueError, match=msg):
    dt_cls([pd.NaT, Timestamp("2011-01-01").value], freq="D")
