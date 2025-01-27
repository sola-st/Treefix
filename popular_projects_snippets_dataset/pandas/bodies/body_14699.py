# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_subplots.py
# GH 9093
df = DataFrame([[1, 2], [2, 5]], columns=["Type A", "Type B"])
df.index.name = index_name

# default is the ylabel is not shown and xlabel is index name
axes = df.plot(kind=kind, subplots=True)
assert all(ax.get_ylabel() == "" for ax in axes)
assert all(ax.get_xlabel() == old_label for ax in axes)

# old xlabel will be overridden and assigned ylabel will be used as ylabel
axes = df.plot(kind=kind, ylabel=new_label, xlabel=new_label, subplots=True)
assert all(ax.get_ylabel() == str(new_label) for ax in axes)
assert all(ax.get_xlabel() == str(new_label) for ax in axes)
