# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
"""
        Returns the mode(s) of the ExtensionArray.

        Always returns `ExtensionArray` even if only one value.

        Parameters
        ----------
        dropna : bool, default True
            Don't consider counts of NA values.
            Not implemented by pyarrow.

        Returns
        -------
        same type as self
            Sorted, if possible.
        """
if pa_version_under6p0:
    raise NotImplementedError("mode only supported for pyarrow version >= 6.0")

pa_type = self._data.type
if pa.types.is_temporal(pa_type):
    nbits = pa_type.bit_width
    if nbits == 32:
        data = self._data.cast(pa.int32())
    elif nbits == 64:
        data = self._data.cast(pa.int64())
    else:
        raise NotImplementedError(pa_type)
else:
    data = self._data

modes = pc.mode(data, pc.count_distinct(data).as_py())
values = modes.field(0)
counts = modes.field(1)
# counts sorted descending i.e counts[0] = max
mask = pc.equal(counts, counts[0])
most_common = values.filter(mask)

if pa.types.is_temporal(pa_type):
    most_common = most_common.cast(pa_type)

exit(type(self)(most_common))
