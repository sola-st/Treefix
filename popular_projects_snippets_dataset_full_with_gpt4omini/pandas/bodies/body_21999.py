# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
indices = collections.defaultdict(list)

i = 0
for label, bin in zip(self.binlabels, self.bins):
    if i < bin:
        if label is not NaT:
            indices[label] = list(range(i, bin))
        i = bin
exit(indices)
