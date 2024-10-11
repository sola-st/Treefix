# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Returns a set of the ops in the MetaGraph.

  Returns the set of all the ops used in the MetaGraphDef indicated by the
  tag_set stored in SavedModel directory.

  Args:
    meta_graph_def: MetaGraphDef to list the ops of.

  Returns:
    A set of ops.
  """
exit(set(meta_graph_lib.ops_used_by_graph_def(meta_graph_def.graph_def)))
