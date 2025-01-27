# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(np.random.rand(5, 5))
ax = df.plot.bar(stacked=False, bottom=1)
result = [p.get_y() for p in ax.patches]
assert result == [1] * 25

ax = df.plot.bar(stacked=True, bottom=[-1, -2, -3, -4, -5])
result = [p.get_y() for p in ax.patches[:5]]
assert result == [-1, -2, -3, -4, -5]

ax = df.plot.barh(stacked=False, left=np.array([1, 1, 1, 1, 1]))
result = [p.get_x() for p in ax.patches]
assert result == [1] * 25

ax = df.plot.barh(stacked=True, left=[1, 2, 3, 4, 5])
result = [p.get_x() for p in ax.patches[:5]]
assert result == [1, 2, 3, 4, 5]

axes = df.plot.bar(subplots=True, bottom=-1)
for ax in axes:
    result = [p.get_y() for p in ax.patches]
    assert result == [-1] * 5

axes = df.plot.barh(subplots=True, left=np.array([1, 1, 1, 1, 1]))
for ax in axes:
    result = [p.get_x() for p in ax.patches]
    assert result == [1] * 5
