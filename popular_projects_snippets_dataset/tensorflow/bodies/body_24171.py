# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/hooks.py
"""Constructs a GrpcDebugHook.

    Args:
      grpc_debug_server_addresses: (`list` of `str`) A list of the gRPC debug
        server addresses, in the format of <host:port>, with or without the
        "grpc://" prefix. For example: ["localhost:7000", "192.168.0.2:8000"]
      watch_fn: A function that allows for customizing which ops to watch at
        which specific steps. See doc of
        `dumping_wrapper.DumpingDebugWrapperSession.__init__` for details.
      thread_name_filter: Regular-expression white list for threads on which the
        wrapper session will be active. See doc of `BaseDebugWrapperSession` for
        more details.
      log_usage: (bool) Whether usage is to be logged.
    """
self._grpc_debug_wrapper_session = None
self._thread_name_filter = thread_name_filter
self._grpc_debug_server_addresses = (
    grpc_debug_server_addresses
    if isinstance(grpc_debug_server_addresses, list) else
    [grpc_debug_server_addresses])

self._watch_fn = watch_fn
self._log_usage = log_usage
