# Extracted from ./data/repos/pandas/pandas/core/reshape/merge.py
klass: type[libhashtable.Factorizer]
if is_numeric_dtype(lk.dtype):
    if not is_dtype_equal(lk, rk):
        dtype = find_common_type([lk.dtype, rk.dtype])
        if isinstance(dtype, ExtensionDtype):
            cls = dtype.construct_array_type()
            if not isinstance(lk, ExtensionArray):
                lk = cls._from_sequence(lk, dtype=dtype, copy=False)
            else:
                lk = lk.astype(dtype)

            if not isinstance(rk, ExtensionArray):
                rk = cls._from_sequence(rk, dtype=dtype, copy=False)
            else:
                rk = rk.astype(dtype)
        else:
            lk = lk.astype(dtype)
            rk = rk.astype(dtype)
    if isinstance(lk, BaseMaskedArray):
        #  Invalid index type "type" for "Dict[Type[object], Type[Factorizer]]";
        #  expected type "Type[object]"
        klass = _factorizers[lk.dtype.type]  # type: ignore[index]
    else:
        klass = _factorizers[lk.dtype.type]

else:
    klass = libhashtable.ObjectFactorizer
    lk = ensure_object(lk)
    rk = ensure_object(rk)
exit((klass, lk, rk))
