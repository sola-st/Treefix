# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
"""Load and process partition graphs.

    Load the graphs; parse the input and control input structure; obtain the
    device and op type of each node; remove the Copy and debug ops inserted
    by the debugger. The gathered information can be used to validate the
    tensor dumps.

    Args:
      client_partition_graphs: A repeated field of GraphDefs representing the
        partition graphs executed by the TensorFlow runtime, from the Python
        client. These partition graphs are used only if partition graphs
        cannot be loaded from the dump directory on the file system.
      validate: (`bool`) Whether the dump files are to be validated against the
        partition graphs.

    Raises:
      ValueError: If the partition GraphDef of one or more devices fail to be
        loaded.
    """
self._debug_graphs = {}
self._node_devices = {}

partition_graphs_and_device_names = []
for device_name in self._device_names:
    partition_graph = None
    if device_name in self._dump_graph_file_paths:
        partition_graph = _load_graph_def_from_event_file(
            self._dump_graph_file_paths[device_name])
    else:
        logging.warn(
            "Failed to load partition graphs for device %s from disk. "
            "As a fallback, the client graphs will be used. This "
            "may cause mismatches in device names." % device_name)
        partition_graph = self._find_partition_graph(client_partition_graphs,
                                                     device_name)

    if partition_graph:
        partition_graphs_and_device_names.append((partition_graph,
                                                  device_name))

for partition_graph, maybe_device_name in partition_graphs_and_device_names:
    debug_graph = debug_graphs.DebugGraph(partition_graph,
                                          device_name=maybe_device_name)
    self._debug_graphs[debug_graph.device_name] = debug_graph
    self._collect_node_devices(debug_graph)

    if validate and debug_graph.device_name in self._dump_tensor_data:
        self._validate_dump_with_graphs(debug_graph.device_name)
