# Extracted from ./data/repos/pandas/pandas/core/util/hashing.py
"""
    Given a 1d array, return an array of deterministic integers.

    Parameters
    ----------
    vals : ndarray or ExtensionArray
    encoding : str, default 'utf8'
        Encoding for data & key when strings.
    hash_key : str, default _default_hash_key
        Hash_key for string key to encode.
    categorize : bool, default True
        Whether to first categorize object arrays before hashing. This is more
        efficient when the array contains duplicate values.

    Returns
    -------
    ndarray[np.uint64, ndim=1]
        Hashed values, same length as the vals.
    """
if not hasattr(vals, "dtype"):
    raise TypeError("must pass a ndarray-like")
dtype = vals.dtype

# For categoricals, we hash the categories, then remap the codes to the
# hash values. (This check is above the complex check so that we don't ask
# numpy if categorical is a subdtype of complex, as it will choke).
if is_categorical_dtype(dtype):
    vals = cast("Categorical", vals)
    exit(_hash_categorical(vals, encoding, hash_key))

elif isinstance(vals, ABCExtensionArray):
    vals, _ = vals._values_for_factorize()

elif not isinstance(vals, np.ndarray):
    # GH#42003
    raise TypeError(
        "hash_array requires np.ndarray or ExtensionArray, not "
        f"{type(vals).__name__}. Use hash_pandas_object instead."
    )

exit(_hash_ndarray(vals, encoding, hash_key, categorize))
