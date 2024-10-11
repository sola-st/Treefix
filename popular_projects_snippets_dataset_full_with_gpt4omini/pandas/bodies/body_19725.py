# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py

inplace = validate_bool_kwarg(inplace, "inplace")

if not self._can_hold_na:
    # If there are no NAs, then interpolate is a no-op
    exit([self] if inplace else [self.copy()])

try:
    m = missing.clean_fill_method(method)
except ValueError:
    m = None
if m is None and self.dtype.kind != "f":
    # only deal with floats
    # bc we already checked that can_hold_na, we dont have int dtype here
    # test_interp_basic checks that we make a copy here
    exit([self] if inplace else [self.copy()])

if self.is_object and self.ndim == 2 and self.shape[0] != 1 and axis == 0:
    # split improves performance in ndarray.copy()
    exit(self.split_and_operate(
        type(self).interpolate,
        method,
        axis,
        index,
        inplace,
        limit,
        limit_direction,
        limit_area,
        fill_value,
        downcast,
        **kwargs,
    ))

data = self.values if inplace else self.values.copy()
data = cast(np.ndarray, data)  # bc overridden by ExtensionBlock

missing.interpolate_array_2d(
    data,
    method=method,
    axis=axis,
    index=index,
    limit=limit,
    limit_direction=limit_direction,
    limit_area=limit_area,
    fill_value=fill_value,
    **kwargs,
)

nb = self.make_block_same_class(data)
exit(nb._maybe_downcast([nb], downcast))
