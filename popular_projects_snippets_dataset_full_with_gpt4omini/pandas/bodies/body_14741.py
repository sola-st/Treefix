# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame({"y": [0.0, 1.0, 2.0, 3.0]}, index=[1.0, 0.0, 3.0, 2.0])
ax = df.plot()
xmin, xmax = ax.get_xlim()
lines = ax.get_lines()
assert xmin <= np.nanmin(lines[0].get_data()[0])
assert xmax >= np.nanmax(lines[0].get_data()[0])

df = DataFrame(
    {"y": [0.0, 1.0, np.nan, 3.0, 4.0, 5.0, 6.0]},
    index=[1.0, 0.0, 3.0, 2.0, np.nan, 3.0, 2.0],
)
ax = df.plot()
xmin, xmax = ax.get_xlim()
lines = ax.get_lines()
assert xmin <= np.nanmin(lines[0].get_data()[0])
assert xmax >= np.nanmax(lines[0].get_data()[0])

df = DataFrame({"y": [0.0, 1.0, 2.0, 3.0], "z": [91.0, 90.0, 93.0, 92.0]})
ax = df.plot(x="z", y="y")
xmin, xmax = ax.get_xlim()
lines = ax.get_lines()
assert xmin <= np.nanmin(lines[0].get_data()[0])
assert xmax >= np.nanmax(lines[0].get_data()[0])
