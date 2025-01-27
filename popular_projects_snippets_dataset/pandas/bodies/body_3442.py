# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_reset_index.py
time = np.arange(0.0, 10, np.sqrt(2) / 2)
s1 = Series(
    (9.81 * time**2) / 2, index=Index(time, name="time"), name="speed"
)
df = DataFrame(s1)

reset = s1.reset_index()
assert reset["time"].dtype == np.float64

reset = df.reset_index()
assert reset["time"].dtype == np.float64
