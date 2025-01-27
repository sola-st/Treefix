# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Enables tracing of op execution via RunMetadata.

  To retrieve the accumulated metadata call context.export_run_metadata()
  and to stop tracing call context.disable_run_metadata().
  """
context().enable_run_metadata()
