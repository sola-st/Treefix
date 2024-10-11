# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# freq being higher-resolution than reso is a problem
msg = "Use a lower freq or a higher unit instead"
with pytest.raises(ValueError, match=msg):
    #    # TODO give a more useful or informative message?
    date_range("2016-01-01", "2016-01-02", freq="ns", unit="ms")
