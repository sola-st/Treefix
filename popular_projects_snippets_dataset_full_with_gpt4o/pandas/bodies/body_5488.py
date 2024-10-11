# Extracted from ./data/repos/pandas/pandas/tests/scalar/timestamp/test_comparisons.py
# don't raise when converting dt64 to Timestamp in __richcmp__
dt = np.datetime64("1066-10-14")
ts = Timestamp(dt)

assert dt == ts
