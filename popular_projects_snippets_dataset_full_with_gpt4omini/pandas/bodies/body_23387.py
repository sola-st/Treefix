# Extracted from ./data/repos/pandas/pandas/core/interchange/column.py
"""
        Return the buffer containing the data and the buffer's associated dtype.
        """
if self.dtype[0] in (
    DtypeKind.INT,
    DtypeKind.UINT,
    DtypeKind.FLOAT,
    DtypeKind.BOOL,
    DtypeKind.DATETIME,
):
    buffer = PandasBuffer(self._col.to_numpy(), allow_copy=self._allow_copy)
    dtype = self.dtype
elif self.dtype[0] == DtypeKind.CATEGORICAL:
    codes = self._col.values._codes
    buffer = PandasBuffer(codes, allow_copy=self._allow_copy)
    dtype = self._dtype_from_pandasdtype(codes.dtype)
elif self.dtype[0] == DtypeKind.STRING:
    # Marshal the strings from a NumPy object array into a byte array
    buf = self._col.to_numpy()
    b = bytearray()

    # TODO: this for-loop is slow; can be implemented in Cython/C/C++ later
    for obj in buf:
        if isinstance(obj, str):
            b.extend(obj.encode(encoding="utf-8"))

            # Convert the byte array to a Pandas "buffer" using
            # a NumPy array as the backing store
    buffer = PandasBuffer(np.frombuffer(b, dtype="uint8"))

    # Define the dtype for the returned buffer
    dtype = (
        DtypeKind.STRING,
        8,
        ArrowCTypes.STRING,
        Endianness.NATIVE,
    )  # note: currently only support native endianness
else:
    raise NotImplementedError(f"Data type {self._col.dtype} not handled yet")

exit((buffer, dtype))
