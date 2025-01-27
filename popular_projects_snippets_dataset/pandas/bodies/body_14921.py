# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_series.py
# GH38865 Verify plot order of a Series
ser = Series(data=data, index=index)
ax = ser.plot(kind="bar")

expected = ser.tolist()
result = [
    patch.get_bbox().ymax
    for patch in sorted(ax.patches, key=lambda patch: patch.get_bbox().xmax)
]
assert expected == result
