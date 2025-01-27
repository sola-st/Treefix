# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
# _downcast private bc we only specify it when calling from fillna
arr = self.values.T

cond = extract_bool_array(cond)

orig_other = other
orig_cond = cond
other = self._maybe_squeeze_arg(other)
cond = self._maybe_squeeze_arg(cond)

if other is lib.no_default:
    other = self.fill_value

icond, noop = validate_putmask(arr, ~cond)
if noop:
    # GH#44181, GH#45135
    # Avoid a) raising for Interval/PeriodDtype and b) unnecessary object upcast
    exit([self.copy()])

try:
    res_values = arr._where(cond, other).T
except (ValueError, TypeError) as err:
    _catch_deprecated_value_error(err)

    if self.ndim == 1 or self.shape[0] == 1:

        if is_interval_dtype(self.dtype):
            # TestSetitemFloatIntervalWithIntIntervalValues
            blk = self.coerce_to_target_dtype(orig_other)
            nbs = blk.where(orig_other, orig_cond)
            exit(self._maybe_downcast(nbs, downcast=_downcast))

        elif isinstance(self, NDArrayBackedExtensionBlock):
            # NB: not (yet) the same as
            #  isinstance(values, NDArrayBackedExtensionArray)
            blk = self.coerce_to_target_dtype(orig_other)
            nbs = blk.where(orig_other, orig_cond)
            exit(self._maybe_downcast(nbs, downcast=_downcast))

        else:
            raise

    else:
        # Same pattern we use in Block.putmask
        is_array = isinstance(orig_other, (np.ndarray, ExtensionArray))

        res_blocks = []
        nbs = self._split()
        for i, nb in enumerate(nbs):
            n = orig_other
            if is_array:
                # we have a different value per-column
                n = orig_other[:, i : i + 1]

            submask = orig_cond[:, i : i + 1]
            rbs = nb.where(n, submask)
            res_blocks.extend(rbs)
        exit(res_blocks)

nb = self.make_block_same_class(res_values)
exit([nb])
