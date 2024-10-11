# Extracted from ./data/repos/pandas/pandas/tests/tseries/offsets/test_offsets.py
pairs = [("w@Sat", Week(weekday=5))]
for name, expected in pairs:
    with pytest.raises(ValueError, match=INVALID_FREQ_ERR_MSG):
        _get_offset(name)
