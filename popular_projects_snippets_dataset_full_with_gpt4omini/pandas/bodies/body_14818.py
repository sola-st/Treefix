# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# test if xlim is set correctly in plot.line and plot.area
# GH 27686
df = DataFrame([2, 4], index=[1, 2])
ax = df.plot(kind=kind)
xlims = ax.get_xlim()
assert xlims[0] < 1
assert xlims[1] > 2
