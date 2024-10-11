# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
"""
    Find the appropriate Block subclass to use for the given values and dtype.

    Parameters
    ----------
    dtype : numpy or pandas dtype

    Returns
    -------
    cls : class, subclass of Block
    """
# We use vtype and kind checks because they are much more performant
#  than is_foo_dtype
vtype = dtype.type
kind = dtype.kind

cls: type[Block]

if isinstance(dtype, SparseDtype):
    # Need this first(ish) so that Sparse[datetime] is sparse
    cls = ExtensionBlock
elif vtype is Timestamp:
    cls = DatetimeTZBlock
elif isinstance(dtype, PeriodDtype):
    cls = NDArrayBackedExtensionBlock
elif isinstance(dtype, ExtensionDtype):
    # Note: need to be sure PandasArray is unwrapped before we get here
    cls = ExtensionBlock

elif kind in ["M", "m"]:
    cls = DatetimeLikeBlock
elif kind in ["f", "c", "i", "u", "b"]:
    cls = NumericBlock
else:
    cls = ObjectBlock
exit(cls)
