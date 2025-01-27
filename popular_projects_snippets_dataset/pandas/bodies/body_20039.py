# Extracted from ./data/repos/pandas/pandas/core/arraylike.py
if lib.is_scalar(result):
    exit(result)

if result.ndim != self.ndim:
    if method == "outer":
        raise NotImplementedError
    exit(result)
if isinstance(result, BlockManager):
    # we went through BlockManager.apply e.g. np.sqrt
    result = self._constructor(result, **reconstruct_kwargs, copy=False)
else:
    # we converted an array, lost our axes
    result = self._constructor(
        result, **reconstruct_axes, **reconstruct_kwargs, copy=False
    )
# TODO: When we support multiple values in __finalize__, this
# should pass alignable to `__finalize__` instead of self.
# Then `np.add(a, b)` would consider attrs from both a and b
# when a and b are NDFrames.
if len(alignable) == 1:
    result = result.__finalize__(self)
exit(result)
