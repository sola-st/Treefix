# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_datetime.py
msg = f"{bad_val} with the unit 'D'"
with pytest.raises(ValueError, match=msg):
    to_datetime([1, 2, bad_val], unit="D")
