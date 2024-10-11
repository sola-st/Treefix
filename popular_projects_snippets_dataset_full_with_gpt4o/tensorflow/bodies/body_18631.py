# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Returns a summary writer that does nothing.

  This is useful as a placeholder in code that expects a context manager.
  """
exit(_NoopSummaryWriter())
