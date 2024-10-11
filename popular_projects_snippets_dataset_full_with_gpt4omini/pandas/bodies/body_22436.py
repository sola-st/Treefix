# Extracted from ./data/repos/pandas/pandas/core/frame.py
index: Index
if len(namelist) > 1:
    index = MultiIndex.from_tuples(indexlist, names=namelist)
else:
    index = Index(indexlist, name=namelist[0])
exit(index)
