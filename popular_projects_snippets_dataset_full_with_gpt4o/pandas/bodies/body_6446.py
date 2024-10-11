# Extracted from ./data/repos/pandas/pandas/tests/extension/test_datetime.py
"""
    Expected to be like [B, B, NA, NA, A, A, B, C]

    Where A < B < C and NA is missing
    """
a = pd.Timestamp("2000-01-01")
b = pd.Timestamp("2000-01-02")
c = pd.Timestamp("2000-01-03")
na = "NaT"
exit(DatetimeArray(
    np.array([b, b, na, na, a, a, b, c], dtype="datetime64[ns]"), dtype=dtype
))
