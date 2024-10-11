# Extracted from ./data/repos/tensorflow/tensorflow/python/summary/writer/writer.py
"""Adds a `MetaGraphDef` to the event file.

    The `MetaGraphDef` allows running the given graph via
    `saver.import_meta_graph()`.

    Args:
      meta_graph_def: A `MetaGraphDef` object, often as returned by
        `saver.export_meta_graph()`.
      global_step: Number. Optional global step counter to record with the
        graph.

    Raises:
      TypeError: If both `meta_graph_def` is not an instance of `MetaGraphDef`.
    """
if not isinstance(meta_graph_def, meta_graph_pb2.MetaGraphDef):
    raise TypeError("meta_graph_def must be type MetaGraphDef, saw type: %s" %
                    type(meta_graph_def))
meta_graph_bytes = meta_graph_def.SerializeToString()
event = event_pb2.Event(meta_graph_def=meta_graph_bytes)
self._add_event(event, global_step)
