# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_timestamp.py
dt64 = np.datetime64(106752, "D")  # won't fit in M8[ns]
ts = Timestamp._from_dt64(dt64)
other = Timestamp(dt64 - 1)

assert other.asm8 < ts
