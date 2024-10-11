# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# GH 37001
xcol = "Type A"
ycol = "Type B"
df = DataFrame([[1, 2], [2, 5]], columns=[xcol, ycol])

# default is the labels are column names
ax = df.plot(kind=kind, x=xcol, y=ycol, xlabel=xlabel, ylabel=ylabel)
assert ax.get_xlabel() == (xcol if xlabel is None else xlabel)
assert ax.get_ylabel() == (ycol if ylabel is None else ylabel)
