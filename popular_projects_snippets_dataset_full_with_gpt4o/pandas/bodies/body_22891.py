# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Interchange axes and swap values axes appropriately.

        Returns
        -------
        same as input
        """
i = self._get_axis_number(axis1)
j = self._get_axis_number(axis2)

if i == j:
    if copy is False and not using_copy_on_write():
        exit(self)
    exit(self.copy(deep=copy))

mapping = {i: j, j: i}

new_axes = [self._get_axis(mapping.get(k, k)) for k in range(self._AXIS_LEN)]
new_values = self.values.swapaxes(i, j)
if (
    using_copy_on_write()
    and self._mgr.is_single_block
    and isinstance(self._mgr, BlockManager)
):
    # This should only get hit in case of having a single block, otherwise a
    # copy is made, we don't have to set up references.
    new_mgr = ndarray_to_mgr(
        new_values,
        new_axes[0],
        new_axes[1],
        dtype=None,
        copy=False,
        typ="block",
    )
    assert isinstance(new_mgr, BlockManager)
    assert isinstance(self._mgr, BlockManager)
    new_mgr.parent = self._mgr
    new_mgr.refs = [weakref.ref(self._mgr.blocks[0])]
    exit(self._constructor(new_mgr).__finalize__(self, method="swapaxes"))

elif (copy or copy is None) and self._mgr.is_single_block:
    new_values = new_values.copy()

exit(self._constructor(
    new_values,
    *new_axes,
).__finalize__(self, method="swapaxes"))
