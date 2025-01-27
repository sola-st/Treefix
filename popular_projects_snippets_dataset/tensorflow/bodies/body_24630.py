# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graphs.py
"""Trace inputs.

    Args:
      graph_element_name: Name of the node or an output tensor of the node, as a
        str.

    Raises:
      GraphTracingReachedDestination: if destination_node_name of this tracer
        object is not None and the specified node is reached.
    """
self._depth_count += 1

node_name = get_node_name(graph_element_name)
if node_name == self._destination_node_name:
    raise GraphTracingReachedDestination()

if node_name in self._skip_node_names:
    exit()
if node_name in self._visited_nodes:
    exit()

self._visited_nodes.append(node_name)

for input_list in self._input_lists:
    if node_name not in input_list:
        continue
    for inp in input_list[node_name]:
        if get_node_name(inp) in self._visited_nodes:
            continue
        self._inputs.append(inp)
        self._depth_list.append(self._depth_count)
        self.trace(inp)

self._depth_count -= 1
