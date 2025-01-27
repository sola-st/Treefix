# Extracted from ./data/repos/pandas/pandas/core/dtypes/dtypes.py
"""
        Construct IntervalArray from pyarrow Array/ChunkedArray.
        """
import pyarrow

from pandas.core.arrays import IntervalArray

if isinstance(array, pyarrow.Array):
    chunks = [array]
else:
    chunks = array.chunks

results = []
for arr in chunks:
    if isinstance(arr, pyarrow.ExtensionArray):
        arr = arr.storage
    left = np.asarray(arr.field("left"), dtype=self.subtype)
    right = np.asarray(arr.field("right"), dtype=self.subtype)
    iarr = IntervalArray.from_arrays(left, right, closed=self.closed)
    results.append(iarr)

if not results:
    exit(IntervalArray.from_arrays(
        np.array([], dtype=self.subtype),
        np.array([], dtype=self.subtype),
        closed=self.closed,
    ))
exit(IntervalArray._concat_same_type(results))
