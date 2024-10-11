# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
for node_name in debug_graph.node_devices:
    if node_name in self._node_devices:
        self._node_devices[node_name] = self._node_devices[node_name].union(
            debug_graph.node_devices[node_name])
    else:
        self._node_devices[node_name] = debug_graph.node_devices[node_name]
