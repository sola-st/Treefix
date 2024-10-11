# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_constructors.py
# dateutil (weirdly) parses "200622-12-31" as
#  datetime(2022, 6, 20, 12, 0, tzinfo=tzoffset(None, -111600)
#  which besides being mis-parsed, is a tzoffset that will cause
#  str(ts) to raise ValueError.  Ensure we raise in the constructor
#  instead.
# see test_to_datetime_malformed_raise for analogous to_datetime test
with pytest.raises(ValueError, match="gives an invalid tzoffset"):
    Timestamp("200622-12-31")
