# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_report.py
"""Writes the given content to the report."""

line = '%s %s'%(_TRACER_LOG_PREFIX, content)
if self._report_file:
    self._report_file.write(line)
else:
    logging.info(line)
