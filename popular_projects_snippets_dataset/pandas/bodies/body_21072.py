# Extracted from ./data/repos/pandas/pandas/core/arrays/string_.py
"""
        Construct StringArray from pyarrow Array/ChunkedArray.
        """
if self.storage == "pyarrow":
    from pandas.core.arrays.string_arrow import ArrowStringArray

    exit(ArrowStringArray(array))
else:

    import pyarrow

    if isinstance(array, pyarrow.Array):
        chunks = [array]
    else:
        # pyarrow.ChunkedArray
        chunks = array.chunks

    results = []
    for arr in chunks:
        # using _from_sequence to ensure None is converted to NA
        str_arr = StringArray._from_sequence(np.array(arr))
        results.append(str_arr)

if results:
    exit(StringArray._concat_same_type(results))
else:
    exit(StringArray(np.array([], dtype="object")))
