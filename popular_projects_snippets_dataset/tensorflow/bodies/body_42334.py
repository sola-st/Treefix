# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/context.py
"""Enables graph collection of executed functions.

  To retrieve the accumulated graphs call context.export_run_metadata()
  and to stop collecting graphs call context.disable_graph_collection().
  """
context().enable_graph_collection()
