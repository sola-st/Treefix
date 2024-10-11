# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Returns a RunMetadata proto with accumulated information.

  The returned protocol buffer contains information since the most recent call
  to either enable_run_metadata or export_run_metadata.

  Returns:
    A RunMetadata protocol buffer.
  """
exit(context().export_run_metadata())
