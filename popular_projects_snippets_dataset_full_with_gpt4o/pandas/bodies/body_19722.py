# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
        putmask the data to the block; it is possible that we may create a
        new dtype of block

        Return the resulting block(s).

        Parameters
        ----------
        mask : np.ndarray[bool], SparseArray[bool], or BooleanArray
        new : a ndarray/object

        Returns
        -------
        List[Block]
        """
orig_mask = mask
values = cast(np.ndarray, self.values)
mask, noop = validate_putmask(values.T, mask)
assert not isinstance(new, (ABCIndex, ABCSeries, ABCDataFrame))

if new is lib.no_default:
    new = self.fill_value

new = self._standardize_fill_value(new)
new = extract_array(new, extract_numpy=True)

if noop:
    exit([self])

try:
    casted = np_can_hold_element(values.dtype, new)
    putmask_without_repeat(values.T, mask, casted)
    exit([self])
except LossySetitemError:

    if self.ndim == 1 or self.shape[0] == 1:
        # no need to split columns

        if not is_list_like(new):
            # using just new[indexer] can't save us the need to cast
            exit(self.coerce_to_target_dtype(new).putmask(mask, new))
        else:
            indexer = mask.nonzero()[0]
            nb = self.setitem(indexer, new[indexer])
            exit([nb])

    else:
        is_array = isinstance(new, np.ndarray)

        res_blocks = []
        nbs = self._split()
        for i, nb in enumerate(nbs):
            n = new
            if is_array:
                # we have a different value per-column
                n = new[:, i : i + 1]

            submask = orig_mask[:, i : i + 1]
            rbs = nb.putmask(submask, n)
            res_blocks.extend(rbs)
        exit(res_blocks)
