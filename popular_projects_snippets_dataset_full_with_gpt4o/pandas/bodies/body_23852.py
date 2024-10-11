# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Get an appropriately typed and shaped pytables.Col object for values.
        """
dtype = values.dtype
# error: Item "ExtensionDtype" of "Union[ExtensionDtype, dtype[Any]]" has no
# attribute "itemsize"
itemsize = dtype.itemsize  # type: ignore[union-attr]

shape = values.shape
if values.ndim == 1:
    # EA, use block shape pretending it is 2D
    # TODO(EA2D): not necessary with 2D EAs
    shape = (1, values.size)

if isinstance(values, Categorical):
    codes = values.codes
    atom = cls.get_atom_data(shape, kind=codes.dtype.name)
elif is_datetime64_dtype(dtype) or is_datetime64tz_dtype(dtype):
    atom = cls.get_atom_datetime64(shape)
elif is_timedelta64_dtype(dtype):
    atom = cls.get_atom_timedelta64(shape)
elif is_complex_dtype(dtype):
    atom = _tables().ComplexCol(itemsize=itemsize, shape=shape[0])
elif is_string_dtype(dtype):
    atom = cls.get_atom_string(shape, itemsize)
else:
    atom = cls.get_atom_data(shape, kind=dtype.name)

exit(atom)
