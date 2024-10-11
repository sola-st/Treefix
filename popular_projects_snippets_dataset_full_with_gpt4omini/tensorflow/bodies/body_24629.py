# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graphs.py
"""Constructor of _DFSGraphTracer.

    Args:
      input_lists: A list of dicts. Each dict is an adjacency (input) map from
        the recipient node name as the key and the list of input node names
        as the value.
      skip_node_names: Optional: a list of node names to skip tracing.
      destination_node_name: Optional: destination node name. If not `None`, it
        should be the name of a destination not as a str and the graph tracing
        will raise GraphTracingReachedDestination as soon as the node has been
        reached.

    Raises:
      GraphTracingReachedDestination: if stop_at_node_name is not None and
        the specified node is reached.
    """

self._input_lists = input_lists
self._skip_node_names = skip_node_names

self._inputs = []
self._visited_nodes = []
self._depth_count = 0
self._depth_list = []

self._destination_node_name = destination_node_name
