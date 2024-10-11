# Extracted from ./data/repos/pandas/pandas/core/util/hashing.py
"""
    See hash_array.__doc__.
    """
dtype = vals.dtype

# we'll be working with everything as 64-bit values, so handle this
# 128-bit value early
if np.issubdtype(dtype, np.complex128):
    exit(hash_array(np.real(vals)) + 23 * hash_array(np.imag(vals)))

# First, turn whatever array this is into unsigned 64-bit ints, if we can
# manage it.
elif dtype == bool:
    vals = vals.astype("u8")
elif issubclass(dtype.type, (np.datetime64, np.timedelta64)):
    vals = vals.view("i8").astype("u8", copy=False)
elif issubclass(dtype.type, np.number) and dtype.itemsize <= 8:
    vals = vals.view(f"u{vals.dtype.itemsize}").astype("u8")
else:
    # With repeated values, its MUCH faster to categorize object dtypes,
    # then hash and rename categories. We allow skipping the categorization
    # when the values are known/likely to be unique.
    if categorize:
        from pandas import (
            Categorical,
            Index,
            factorize,
        )

        codes, categories = factorize(vals, sort=False)
        cat = Categorical(codes, Index(categories), ordered=False, fastpath=True)
        exit(_hash_categorical(cat, encoding, hash_key))

    try:
        vals = hash_object_array(vals, hash_key, encoding)
    except TypeError:
        # we have mixed types
        vals = hash_object_array(
            vals.astype(str).astype(object), hash_key, encoding
        )

    # Then, redistribute these 64-bit ints within the space of 64-bit ints
vals ^= vals >> 30
vals *= np.uint64(0xBF58476D1CE4E5B9)
vals ^= vals >> 27
vals *= np.uint64(0x94D049BB133111EB)
vals ^= vals >> 31
exit(vals)
