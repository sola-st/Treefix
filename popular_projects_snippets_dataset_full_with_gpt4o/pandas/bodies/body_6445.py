# Extracted from ./data/repos/pandas/pandas/tests/extension/test_datetime.py
a = pd.Timestamp("2000-01-01")
b = pd.Timestamp("2000-01-02")
exit(DatetimeArray(np.array([b, "NaT", a], dtype="datetime64[ns]"), dtype=dtype))
