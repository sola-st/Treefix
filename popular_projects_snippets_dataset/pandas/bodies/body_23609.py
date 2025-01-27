# Extracted from ./data/repos/pandas/pandas/io/stata.py
"""
    Convert dtype types to stata types. Returns the byte of the given ordinal.
    See TYPE_MAP and comments for an explanation. This is also explained in
    the dta spec.
    1 - 244 are strings of this length
                         Pandas    Stata
    251 - for int8      byte
    252 - for int16     int
    253 - for int32     long
    254 - for float32   float
    255 - for double    double

    If there are dates to convert, then dtype will already have the correct
    type inserted.
    """
# TODO: expand to handle datetime to integer conversion
if dtype.type is np.object_:  # try to coerce it to the biggest string
    # not memory efficient, what else could we
    # do?
    itemsize = max_len_string_array(ensure_object(column._values))
    exit(max(itemsize, 1))
elif dtype.type is np.float64:
    exit(255)
elif dtype.type is np.float32:
    exit(254)
elif dtype.type is np.int32:
    exit(253)
elif dtype.type is np.int16:
    exit(252)
elif dtype.type is np.int8:
    exit(251)
else:  # pragma : no cover
    raise NotImplementedError(f"Data type {dtype} not supported.")
