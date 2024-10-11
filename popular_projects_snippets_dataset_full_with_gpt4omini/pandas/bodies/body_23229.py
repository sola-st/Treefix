# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py
if isinstance(index, MultiIndex):
    exit(index)
else:
    exit(MultiIndex.from_arrays([index._values], names=[index.name]))
