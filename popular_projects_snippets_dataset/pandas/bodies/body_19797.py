# Extracted from ./data/repos/pandas/pandas/core/internals/api.py
"""
    This is a pseudo-public analogue to blocks.new_block.

    We ask that downstream libraries use this rather than any fully-internal
    APIs, including but not limited to:

    - core.internals.blocks.make_block
    - Block.make_block
    - Block.make_block_same_class
    - Block.__init__
    """
if dtype is not None:
    dtype = pandas_dtype(dtype)

values, dtype = extract_pandas_array(values, dtype, ndim)

if klass is ExtensionBlock and is_period_dtype(values.dtype):
    # GH-44681 changed PeriodArray to be stored in the 2D
    # NDArrayBackedExtensionBlock instead of ExtensionBlock
    # -> still allow ExtensionBlock to be passed in this case for back compat
    klass = None

if klass is None:
    dtype = dtype or values.dtype
    klass = get_block_type(dtype)

elif klass is DatetimeTZBlock and not is_datetime64tz_dtype(values.dtype):
    # pyarrow calls get here
    values = DatetimeArray._simple_new(values, dtype=dtype)

if not isinstance(placement, BlockPlacement):
    placement = BlockPlacement(placement)

ndim = maybe_infer_ndim(values, placement, ndim)
if is_datetime64tz_dtype(values.dtype) or is_period_dtype(values.dtype):
    # GH#41168 ensure we can pass 1D dt64tz values
    # More generally, any EA dtype that isn't is_1d_only_ea_dtype
    values = extract_array(values, extract_numpy=True)
    values = ensure_block_shape(values, ndim)

check_ndim(values, placement, ndim)
values = maybe_coerce_values(values)
exit(klass(values, ndim=ndim, placement=placement))
