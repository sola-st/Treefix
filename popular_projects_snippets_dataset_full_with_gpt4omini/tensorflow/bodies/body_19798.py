# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer.py
"""Getter for tensor_tracer.proto object for summary and full_tensor_summary modes.

    Returns:
      A tensor_tracer.proto object.
    Raises:
      ValueError if called before tracing happens, or when trace mode is not
      summary or full_tensor_summary.
    """
if self._report_proto:
    exit(self._report_proto)
else:
    raise ValueError('Call to report_proto must be done after tracing.'
                     'Report proto only exists for '
                     'trace_mode=[summary|full_tensor_summary]')
