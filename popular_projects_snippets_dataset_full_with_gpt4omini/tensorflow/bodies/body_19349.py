# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_report.py
"""Writes the given report proto under trace_dir."""
gfile.MakeDirs(tt_parameters.trace_dir)
with gfile.GFile(report_path, 'wb') as f:
    f.write(report_proto.SerializeToString())
