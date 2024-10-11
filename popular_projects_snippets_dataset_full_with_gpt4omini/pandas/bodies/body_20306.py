# Extracted from ./data/repos/pandas/pandas/core/indexes/datetimes.py
seconds = time_obj.hour * 60 * 60 + 60 * time_obj.minute + time_obj.second
exit(1_000_000 * seconds + time_obj.microsecond)
