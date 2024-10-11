# Extracted from ./data/repos/pandas/pandas/tests/tools/test_to_numeric.py
ser = Series(data)

with pytest.raises(ValueError, match=msg):
    to_numeric(ser, errors="raise")
