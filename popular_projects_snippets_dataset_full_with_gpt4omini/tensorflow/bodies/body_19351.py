# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_report.py
"""Writes the list of checkpoints."""
self._write_report('%s %s\n'%(_MARKER_SECTION_BEGIN,
                              _SECTION_NAME_TENSOR_TRACER_CHECKPOINT))
for (tensor, checkpoint_name) in tensor_trace_points:
    self._write_report('%s %s\n'%(tensor.name, checkpoint_name))
self._write_report('%s %s\n'%(_MARKER_SECTION_END,
                              _SECTION_NAME_TENSOR_TRACER_CHECKPOINT))
