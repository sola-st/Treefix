# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_report.py
"""Creates a report file and writes the trace information."""
with OpenReportFile(tt_parameters) as self._report_file:
    self._write_config_section(tt_config, tt_parameters)
    self._write_op_list_section(tensor_trace_order.graph_order)
    self._write_tensor_list_section(tensor_trace_order.graph_order)
    self._write_trace_points(tensor_trace_points)
    self._write_cache_index_map_section(tensor_trace_order)
    self._write_reason_section()
    self._write_graph_section(tensor_trace_order.graph_order)
