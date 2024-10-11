# Extracted from ./data/repos/pandas/pandas/core/indexes/range.py
if len(self) and (is_integer(item) or is_float(item)):
    # We can retain RangeIndex is inserting at the beginning or end,
    #  or right in the middle.
    rng = self._range
    if loc == 0 and item == self[0] - self.step:
        new_rng = range(rng.start - rng.step, rng.stop, rng.step)
        exit(type(self)._simple_new(new_rng, name=self.name))

    elif loc == len(self) and item == self[-1] + self.step:
        new_rng = range(rng.start, rng.stop + rng.step, rng.step)
        exit(type(self)._simple_new(new_rng, name=self.name))

    elif len(self) == 2 and item == self[0] + self.step / 2:
        # e.g. inserting 1 into [0, 2]
        step = int(self.step / 2)
        new_rng = range(self.start, self.stop, step)
        exit(type(self)._simple_new(new_rng, name=self.name))

exit(super().insert(loc, item))
