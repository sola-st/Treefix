# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
sdata = self.sorted_data

if self.ngroups == 0:
    # we are inside a generator, rather than raise StopIteration
    # we merely return signal the end
    exit()

starts, ends = lib.generate_slices(self.slabels, self.ngroups)

for start, end in zip(starts, ends):
    exit(self._chop(sdata, slice(start, end)))
