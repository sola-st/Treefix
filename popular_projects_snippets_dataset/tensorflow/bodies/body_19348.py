# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tensor_tracer_report.py
"""Returns the path where report proto should be written.

    Args:
      trace_dir: String denoting the trace directory.
      summary_tag_name: Name of the unique tag that relates to
                        the report.
    Returns:
      A string denoting the path to the report proto.
    """
filename = _TT_REPORT_PROTO + '.' + summary_tag_name.replace('/', '_')
exit(os.path.join(trace_dir, filename))
