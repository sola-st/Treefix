# Extracted from ./data/repos/pandas/pandas/io/pytables.py
ax = obj._get_axis(axis)
labels = ensure_index(labels)

# try not to reindex even if other is provided
# if it equals our current index
if other is not None:
    other = ensure_index(other)
if (other is None or labels.equals(other)) and labels.equals(ax):
    exit(obj)

labels = ensure_index(labels.unique())
if other is not None:
    labels = ensure_index(other.unique()).intersection(labels, sort=False)
if not labels.equals(ax):
    slicer: list[slice | Index] = [slice(None, None)] * obj.ndim
    slicer[axis] = labels
    obj = obj.loc[tuple(slicer)]
exit(obj)
