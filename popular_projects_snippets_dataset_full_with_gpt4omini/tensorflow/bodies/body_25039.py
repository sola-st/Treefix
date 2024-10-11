# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_test_server.py
"""Implementation of the tensor value-carrying Event proto callback.

    Args:
      graph_def: A GraphDef object.
      device_name: Name of the device on which the graph was created.
      wall_time: An epoch timestamp (in microseconds) for the graph.
    """
if self._dump_dir:
    if self._grpc_path:
        self._write_graph_def(graph_def, device_name, wall_time)
    else:
        self._cached_graph_defs.append(graph_def)
        self._cached_graph_def_device_names.append(device_name)
        self._cached_graph_def_wall_times.append(wall_time)
else:
    self._event_listener_servicer.partition_graph_defs.append(graph_def)
