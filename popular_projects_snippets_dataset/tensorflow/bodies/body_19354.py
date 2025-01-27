# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_report.py
"""Writes the reason section of the report."""

self._write_report('%s %s\n'%(_MARKER_SECTION_BEGIN, _SECTION_NAME_REASON))
for key in sorted(self.instrument_records):
    self._write_report('"%s" %s\n'%(key, self.instrument_records[key]))
self._write_report('%s %s\n'%(_MARKER_SECTION_END, _SECTION_NAME_REASON))
