# Extracted from ./data/repos/pandas/pandas/tests/indexes/categorical/test_category.py
if dtype != np.int64:
    # num. of uniques required to push CategoricalIndex.codes to a
    # dtype (128 categories required for .codes dtype to be int16 etc.)
    num_uniques = {np.int8: 1, np.int16: 128, np.int32: 32768}[dtype]
    ci = CategoricalIndex(range(num_uniques))
else:
    # having 2**32 - 2**31 categories would be very memory-intensive,
    # so we cheat a bit with the dtype
    ci = CategoricalIndex(range(32768))  # == 2**16 - 2**(16 - 1)
    arr = ci.values._ndarray.astype("int64")
    NDArrayBacked.__init__(ci._data, arr, ci.dtype)
assert np.issubdtype(ci.codes.dtype, dtype)
assert isinstance(ci._engine, engine_type)
