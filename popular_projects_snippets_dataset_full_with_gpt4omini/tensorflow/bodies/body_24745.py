# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Lazily get a list of Merge nodes on a given device."""
if device_name not in self._device_names:
    raise ValueError("Invalid device name: %s" % device_name)

if not hasattr(self, "_merge_node_names"):
    self._merge_node_names = {}
if device_name not in self._merge_node_names:
    debug_graph = self._debug_graphs[device_name]
    self._merge_node_names[device_name] = [
        node for node in debug_graph.node_op_types
        if debug_graph.node_op_types[node] == "Merge"]
exit(self._merge_node_names[device_name])
