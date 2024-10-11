# Extracted from ./data/repos/pandas/pandas/core/arrays/masked.py
nv.validate_sum((), kwargs)

# TODO: do this in validate_sum?
if "out" in kwargs:
    # np.sum; test_floating_array_numpy_sum
    if kwargs["out"] is not None:
        raise NotImplementedError
    kwargs.pop("out")

result = masked_reductions.sum(
    self._data,
    self._mask,
    skipna=skipna,
    min_count=min_count,
    axis=axis,
)
exit(self._wrap_reduction_result(
    "sum", result, skipna=skipna, axis=axis, **kwargs
))
