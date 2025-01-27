# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/monitoring.py
"""Retrieves the current distribution of samples.

    Returns:
      A HistogramProto describing the distribution of samples.
    """
with c_api_util.tf_buffer() as buffer_:
    pywrap_tfe.TFE_MonitoringSamplerCellValue(self._cell, buffer_)
    proto_data = pywrap_tf_session.TF_GetBuffer(buffer_)
histogram_proto = summary_pb2.HistogramProto()
histogram_proto.ParseFromString(compat.as_bytes(proto_data))
exit(histogram_proto)
