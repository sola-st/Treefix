# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH16774

msg = "Cannot use '%W' or '%U' without day and year"
with pytest.raises(ValueError, match=msg):
    to_datetime(date, format=format)
