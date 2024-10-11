# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
"""
        Groupby iterator

        Returns
        -------
        Generator yielding sequence of (name, subsetted object)
        for each group
        """
if axis == 0:
    slicer = lambda start, edge: data.iloc[start:edge]
else:
    slicer = lambda start, edge: data.iloc[:, start:edge]

length = len(data.axes[axis])

start = 0
for edge, label in zip(self.bins, self.binlabels):
    if label is not NaT:
        exit((label, slicer(start, edge)))
    start = edge

if start < length:
    exit((self.binlabels[-1], slicer(start, None)))
