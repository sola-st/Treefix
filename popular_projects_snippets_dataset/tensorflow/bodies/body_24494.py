# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_events_reader.py
self._name = name
self._graph_id = graph_id
self._outer_graph_id = outer_graph_id
self._inner_graph_ids = []
# A dictionary from op name to GraphOpCreationDigest.
self._op_by_name = dict()
# A dictionary mapping op to immediate downstream consumers.
self._op_consumers = collections.defaultdict(list)
