# Extracted from ./data/repos/pandas/pandas/tests/arrays/test_datetimelike.py
msg = (
    "value should be a '(Timestamp|Timedelta|Period)', 'NaT', or array of those. "
    "Got '(timedelta64|datetime64|int)' instead."
)

for nat in non_casting_nats:
    with pytest.raises(TypeError, match=msg):
        arr[0] = nat
