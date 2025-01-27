# Extracted from ./data/repos/pandas/pandas/tests/extension/test_datetime.py
a = pd.Timestamp("2000-01-01")
b = pd.Timestamp("2000-01-02")
c = pd.Timestamp("2000-01-03")
exit(DatetimeArray(np.array([b, c, a], dtype="datetime64[ns]"), dtype=dtype))
