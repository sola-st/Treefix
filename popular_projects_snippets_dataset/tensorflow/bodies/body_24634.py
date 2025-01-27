# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_graphs.py
self._debug_graph_def = debug_graph_def
self._non_debug_graph_def = None

self._node_attributes = {}
self._node_inputs = {}
self._node_reversed_ref_inputs = {}
self._node_ctrl_inputs = {}
self._node_recipients = {}
self._node_ctrl_recipients = {}
self._node_devices = {}
self._node_op_types = {}
self._copy_send_nodes = []
self._ref_args = {}

self._device_name = device_name
if not self._device_name:
    self._device_name = _infer_device_name(debug_graph_def)

for node in debug_graph_def.node:
    self._process_debug_graph_node(node)

self._prune_non_control_edges_of_debug_ops()
self._prune_control_edges_of_debug_ops()
self._prune_nodes_from_input_and_recipient_maps(self._get_copy_nodes())

self._populate_recipient_maps()
