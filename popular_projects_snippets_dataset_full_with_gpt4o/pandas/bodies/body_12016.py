# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_parse_dates.py
try:
    arr = dt + "T" + time
except TypeError:
    # dt & time are date/time objects
    arr = [datetime.combine(d, t) for d, t in zip(dt, time)]
exit(np.array(arr, dtype="datetime64[s]"))
