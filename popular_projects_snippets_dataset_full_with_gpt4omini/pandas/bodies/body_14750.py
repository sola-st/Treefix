# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(np.random.randn(5, 5))

width = 0.9

# regular
ax = df.plot.bar(width=width)
for r in ax.patches:
    assert r.get_width() == width / len(df.columns)

# stacked
ax = df.plot.bar(stacked=True, width=width)
for r in ax.patches:
    assert r.get_width() == width

# horizontal regular
ax = df.plot.barh(width=width)
for r in ax.patches:
    assert r.get_height() == width / len(df.columns)

# horizontal stacked
ax = df.plot.barh(stacked=True, width=width)
for r in ax.patches:
    assert r.get_height() == width

# subplots
axes = df.plot.bar(width=width, subplots=True)
for ax in axes:
    for r in ax.patches:
        assert r.get_width() == width

        # horizontal subplots
axes = df.plot.barh(width=width, subplots=True)
for ax in axes:
    for r in ax.patches:
        assert r.get_height() == width
