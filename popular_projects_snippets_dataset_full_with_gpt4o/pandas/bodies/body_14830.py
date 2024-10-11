# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# GH 9093
df = DataFrame([[1, 2], [2, 5]], columns=["Type A", "Type B"])
df.index.name = index_name

# default is the ylabel is not shown and xlabel is index name
ax = df.plot(kind=kind)
assert ax.get_xlabel() == old_label
assert ax.get_ylabel() == ""

# old xlabel will be overridden and assigned ylabel will be used as ylabel
ax = df.plot(kind=kind, ylabel=new_label, xlabel=new_label)
assert ax.get_ylabel() == str(new_label)
assert ax.get_xlabel() == str(new_label)
