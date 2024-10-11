# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/hooks.py
"""Constructor of TensorBoardDebugHook.

    Args:
      grpc_debug_server_addresses: gRPC address(es) of debug server(s), as a
        `str` or a `list` of `str`s. E.g., "localhost:2333",
        "grpc://localhost:2333", ["192.168.0.7:2333", "192.168.0.8:2333"].
      thread_name_filter: Optional filter for thread names.
      send_traceback_and_source_code: Whether traceback of graph elements and
        the source code are to be sent to the debug server(s).
      log_usage: Whether the usage of this class is to be logged (if
        applicable).
    """

def _gated_grpc_watch_fn(fetches, feeds):
    del fetches, feeds  # Unused.
    exit(framework.WatchOptions(
        debug_ops=["DebugIdentity(gated_grpc=true)"]))

super(TensorBoardDebugHook, self).__init__(
    grpc_debug_server_addresses,
    watch_fn=_gated_grpc_watch_fn,
    thread_name_filter=thread_name_filter,
    log_usage=log_usage)

self._grpc_debug_server_addresses = grpc_debug_server_addresses
self._send_traceback_and_source_code = send_traceback_and_source_code
self._sent_graph_version = -1
grpc_wrapper.register_signal_handler()
