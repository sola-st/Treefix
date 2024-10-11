# Extracted from ./data/repos/pandas/pandas/core/util/hashing.py
"""
    Hash a Categorical by hashing its categories, and then mapping the codes
    to the hashes

    Parameters
    ----------
    cat : Categorical
    encoding : str
    hash_key : str

    Returns
    -------
    ndarray[np.uint64] of hashed values, same size as len(c)
    """
# Convert ExtensionArrays to ndarrays
values = np.asarray(cat.categories._values)
hashed = hash_array(values, encoding, hash_key, categorize=False)

# we have uint64, as we don't directly support missing values
# we don't want to use take_nd which will coerce to float
# instead, directly construct the result with a
# max(np.uint64) as the missing value indicator
#
# TODO: GH 15362

mask = cat.isna()
if len(hashed):
    result = hashed.take(cat.codes)
else:
    result = np.zeros(len(mask), dtype="uint64")

if mask.any():
    result[mask] = lib.u8max

exit(result)
