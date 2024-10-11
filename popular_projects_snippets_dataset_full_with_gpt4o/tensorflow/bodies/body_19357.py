# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_report.py
"""Writes the mapping from cache index to tensor index to the report."""
self._write_report('%s %s\n'%(_MARKER_SECTION_BEGIN,
                              _SECTION_NAME_CACHE_INDEX_MAP))
self._write_report('%s %d\n'%(
    _FIELD_NAME_NUM_CACHE_INDICES,
    len(tensor_trace_order.cache_idx_to_tensor_idx)))
for cache_idx in range(0, len(tensor_trace_order.cache_idx_to_tensor_idx)):
    tensor_idx = tensor_trace_order.cache_idx_to_tensor_idx[cache_idx]
    line = '%d %d\n'%(cache_idx, tensor_idx)
    self._write_report(line)
self._write_report('%s %s\n'%(_MARKER_SECTION_END,
                              _SECTION_NAME_CACHE_INDEX_MAP))
