# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
dates = [(datetime(2012, 9, 9, 0, 0), datetime(2012, 9, 8, 15, 10))]
arr = np.array(dates, dtype=[("Date", "M8[us]"), ("Forecasting", "M8[us]")])
df = DataFrame(arr)

assert df["Date"][0] == dates[0][0]
assert df["Forecasting"][0] == dates[0][1]

s = Series(arr["Date"])
assert isinstance(s[0], Timestamp)
assert s[0] == dates[0][0]
