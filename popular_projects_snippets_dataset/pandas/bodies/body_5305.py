# Extracted from ./data/repos/pandas/pandas/tests/scalar/period/test_period.py
msg = "Buffer dtype mismatch, expected 'const int64_t' but got 'double'"
with pytest.raises(ValueError, match=msg):
    libperiod.get_period_field_arr(-1, np.empty(1), 0)
