# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/row_partition.py
"""Checks if the object is internally consistent.

    Raises:
      ValueError if inconsistent.
    """
my_dtype = self.dtype
if self._uniform_row_length is not None:
    if self._uniform_row_length.dtype != my_dtype:
        raise ValueError("_uniform_row_length.dtype=" +
                         str(self._uniform_row_length.dtype) + ", not " +
                         str(my_dtype))

if self._row_lengths is not None and self._row_lengths.dtype != my_dtype:
    raise ValueError("_row_lengths.dtype=" + str(self._row_lengths.dtype) +
                     ", not " + str(my_dtype))

if self._value_rowids is not None and self._value_rowids.dtype != my_dtype:
    raise ValueError("_value_rowids.dtype=" + str(self._value_rowids.dtype) +
                     ", not " + str(my_dtype))

if self._nrows is not None and self._nrows.dtype != my_dtype:
    raise ValueError("_nrows.dtype=" + str(self._nrows.dtype) + ", not " +
                     str(my_dtype))
