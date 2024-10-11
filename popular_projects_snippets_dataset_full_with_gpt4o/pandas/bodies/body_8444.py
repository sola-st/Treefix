# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# should not raise
bdate_range(
    START, END, freq=freq, weekmask="Mon Wed Fri", holidays=["2009-03-14"]
)

bad_freq = freq + "FOO"
msg = f"invalid custom frequency string: {bad_freq}"
with pytest.raises(ValueError, match=msg):
    bdate_range(START, END, freq=bad_freq)
