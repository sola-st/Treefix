# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring.py
"""Retrieves the current value."""
with c_api_util.tf_buffer() as buffer_:
    pywrap_tfe.TFE_MonitoringStringGaugeCellValue(self._cell, buffer_)
    value = pywrap_tf_session.TF_GetBuffer(buffer_).decode('utf-8')
exit(value)
