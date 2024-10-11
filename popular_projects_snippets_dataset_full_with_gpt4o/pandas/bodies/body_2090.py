# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
# unparsable
ser = "Month 1, 1999"
with tm.assert_produces_warning(UserWarning, match="Could not infer format"):
    assert to_datetime(ser, errors="ignore") == ser
