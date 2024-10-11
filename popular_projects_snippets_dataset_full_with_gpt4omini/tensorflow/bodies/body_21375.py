# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Adds a collection to MetaGraphDef protocol buffer.

    Args:
      meta_graph_def: MetaGraphDef protocol buffer.
      key: One of the GraphKeys or user-defined string.
      export_scope: Optional `string`. Name scope to remove.
    """
meta_graph.add_collection_def(
    meta_graph_def, key, export_scope=export_scope)
