# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/xla/xla.py
"""Enters a context where all summary ops are skipped.

  Summaries are not yet supported in xla.compile(). So we provide this context
  manager that can skip creating summary ops. This is a temporary workaround due
  to XLA not supporting summary ops.

  Yields:
    None.
  """
original_skip_summary_func = summary_op_util.skip_summary
summary_op_util.skip_summary = lambda: True

try:
    exit()
finally:
    summary_op_util.skip_summary = original_skip_summary_func
