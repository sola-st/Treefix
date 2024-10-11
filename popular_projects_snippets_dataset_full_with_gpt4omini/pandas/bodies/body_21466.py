# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
order = "ascending" if ascending else "descending"
null_placement = {"last": "at_end", "first": "at_start"}.get(na_position, None)
if null_placement is None or pa_version_under7p0:
    # Although pc.array_sort_indices exists in version 6
    # there's a bug that affects the pa.ChunkedArray backing
    # https://issues.apache.org/jira/browse/ARROW-12042
    fallback_performancewarning("7")
    exit(super().argsort(
        ascending=ascending, kind=kind, na_position=na_position
    ))

result = pc.array_sort_indices(
    self._data, order=order, null_placement=null_placement
)
np_result = result.to_numpy()
exit(np_result.astype(np.intp, copy=False))
