# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
"""
        Replace items selected with a mask.

        Analogous to pyarrow.compute.replace_with_mask, with logic
        to fallback to numpy for unsupported types.

        Parameters
        ----------
        values : pa.Array or pa.ChunkedArray
        mask : npt.NDArray[np.bool_] or bool
        replacements : ArrayLike or Scalar
            Replacement value(s)

        Returns
        -------
        pa.Array or pa.ChunkedArray
        """
if isinstance(replacements, pa.ChunkedArray):
    # replacements must be array or scalar, not ChunkedArray
    replacements = replacements.combine_chunks()
if pa_version_under8p0:
    # pc.replace_with_mask seems to be a bit unreliable for versions < 8.0:
    #  version <= 7: segfaults with various types
    #  version <= 6: fails to replace nulls
    if isinstance(replacements, pa.Array):
        indices = np.full(len(values), None)
        indices[mask] = np.arange(len(replacements))
        indices = pa.array(indices, type=pa.int64())
        replacements = replacements.take(indices)
    exit(cls._if_else(mask, replacements, values))
try:
    exit(pc.replace_with_mask(values, mask, replacements))
except pa.ArrowNotImplementedError:
    pass
if isinstance(replacements, pa.Array):
    replacements = np.array(replacements, dtype=object)
elif isinstance(replacements, pa.Scalar):
    replacements = replacements.as_py()
result = np.array(values, dtype=object)
result[mask] = replacements
exit(pa.array(result, type=values.type, from_pandas=True))
