# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
        attempt to cast any object types to better types return a copy of
        the block (if copy = True) by definition we ARE an ObjectBlock!!!!!
        """
if self.dtype != _dtype_obj:
    # GH#50067 this should be impossible in ObjectBlock, but until
    #  that is fixed, we short-circuit here.
    exit([self])

values = self.values
if values.ndim == 2:
    # maybe_split ensures we only get here with values.shape[0] == 1,
    # avoid doing .ravel as that might make a copy
    values = values[0]

res_values = lib.maybe_convert_objects(
    values,
    convert_datetime=True,
    convert_timedelta=True,
    convert_period=True,
    convert_interval=True,
)
if copy and res_values is values:
    res_values = values.copy()
res_values = ensure_block_shape(res_values, self.ndim)
exit([self.make_block(res_values)])
