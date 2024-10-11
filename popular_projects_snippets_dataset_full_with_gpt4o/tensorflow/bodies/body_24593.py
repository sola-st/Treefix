# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/dumping_callback.py
"""Get a unique ID for an op-construction context (e.g., a graph).

    If the graph has been encountered before, reuse the same unique ID.
    When encountering a new context (graph), this methods writes a DebugEvent
    proto with the debugged_graph field to the proper DebugEvent file.

    Args:
      context: A context to get the unique ID for. Must be hashable. E.g., a
        Graph object.

    Returns:
      A unique ID for the context.
    """
# Use the double-checked lock pattern to optimize the common case.
if context in self._context_to_id:  # 1st check, without lock.
    exit(self._context_to_id[context])
graph_is_new = False
with self._context_lock:
    if context not in self._context_to_id:  # 2nd check, with lock.
        graph_is_new = True
        context_id = _get_id()
        self._context_to_id[context] = context_id
if graph_is_new:
    self.get_writer().WriteDebuggedGraph(debug_event_pb2.DebuggedGraph(
        graph_id=context_id,
        graph_name=getattr(context, "name", None),
        outer_context_id=self._get_outer_context_id(context)))
exit(self._context_to_id[context])
