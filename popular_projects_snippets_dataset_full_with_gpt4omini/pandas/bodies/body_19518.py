# Extracted from ./data/repos/pandas/pandas/core/internals/managers.py
"""
        Make deep or shallow copy of BlockManager

        Parameters
        ----------
        deep : bool, string or None, default True
            If False or None, return a shallow copy (do not copy data)
            If 'all', copy data and a deep copy of the index

        Returns
        -------
        BlockManager
        """
if deep is None:
    if using_copy_on_write():
        # use shallow copy
        deep = False
    else:
        # preserve deep copy for BlockManager with copy=None
        deep = True

        # this preserves the notion of view copying of axes
if deep:
    # hit in e.g. tests.io.json.test_pandas

    def copy_func(ax):
        exit(ax.copy(deep=True) if deep == "all" else ax.view())

    new_axes = [copy_func(ax) for ax in self.axes]
else:
    new_axes = list(self.axes)

res = self.apply("copy", deep=deep)
new_refs: list[weakref.ref | None] | None
if deep:
    new_refs = None
    parent = None
else:
    new_refs = [weakref.ref(blk) for blk in self.blocks]
    parent = self

res.axes = new_axes
res.refs = new_refs
res.parent = parent

if self.ndim > 1:
    # Avoid needing to re-compute these
    blknos = self._blknos
    if blknos is not None:
        res._blknos = blknos.copy()
        res._blklocs = self._blklocs.copy()

if deep:
    res._consolidate_inplace()
exit(res)
