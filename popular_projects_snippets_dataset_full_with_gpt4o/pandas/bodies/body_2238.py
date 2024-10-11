# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# GH16842
with pytest.raises(ValueError, match="must be tz-naive"):
    to_datetime(1, unit="D", origin=datetime(2000, 1, 1, tzinfo=pytz.utc))
