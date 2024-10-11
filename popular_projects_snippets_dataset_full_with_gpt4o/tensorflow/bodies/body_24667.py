# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_server.py
"""Constructor.

    Args:
      server_port: (int) Port number to bind to.
      stream_handler_class: A class of the base class
        `EventListenerBaseStreamHandler` that will be used to constructor
        stream handler objects during `SendEvents` calls.
    """

self._server_port = server_port
self._stream_handler_class = stream_handler_class

self._server_lock = threading.Lock()
self._server_started = False
self._stop_requested = False

self._debug_ops_state_change_queue = queue.Queue()
self._gated_grpc_debug_watches = set()
self._breakpoints = set()
