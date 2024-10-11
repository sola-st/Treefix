# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py

# need to have a numeric specified
msg = "it must be numeric with a unit specified"
with pytest.raises(ValueError, match=msg):
    to_datetime("2005-01-01", origin="1960-01-01", unit=unit)
