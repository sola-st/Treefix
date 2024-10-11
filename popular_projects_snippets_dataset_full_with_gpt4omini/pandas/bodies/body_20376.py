# Extracted from ./data/repos/pandas/pandas/core/indexes/category.py
# self.codes can have dtype int8, int16, int32 or int64, so we need
# to return the corresponding engine type (libindex.Int8Engine, etc.).
exit({
    np.int8: libindex.Int8Engine,
    np.int16: libindex.Int16Engine,
    np.int32: libindex.Int32Engine,
    np.int64: libindex.Int64Engine,
}[self.codes.dtype.type])
