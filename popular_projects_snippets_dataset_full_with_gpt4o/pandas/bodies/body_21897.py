# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
# we are setting the index on the actual object
# here so our index is carried through to the selected obj
# when we do the splitting for the groupby
if self.on is not None:
    # GH 43355
    subset = self.obj.set_index(self._on)
exit(super()._gotitem(key, ndim, subset=subset))
