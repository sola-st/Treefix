# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/grpc_wrapper.py
"""Constructor of TensorBoardDebugWrapperSession.

    Args:
      sess: The `tf.compat.v1.Session` instance to be wrapped.
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

super().__init__(
    sess,
    grpc_debug_server_addresses,
    watch_fn=_gated_grpc_watch_fn,
    thread_name_filter=thread_name_filter,
    log_usage=log_usage)

self._send_traceback_and_source_code = send_traceback_and_source_code
# Keeps track of the latest version of Python graph object that has been
# sent to the debug servers.
self._sent_graph_version = -1

register_signal_handler()
