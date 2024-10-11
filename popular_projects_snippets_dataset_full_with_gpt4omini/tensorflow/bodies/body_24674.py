# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_server.py
"""Request server stopping.

    Once stopped, server cannot be stopped or started again. This method is
    non-blocking. Call `wait()` on the returned event to block until the server
    has completely stopped.

    Args:
      grace: Grace period in seconds to be used when calling `server.stop()`.

    Raises:
      ValueError: If server stop has already been requested, or if the server
        has not started running yet.

    Returns:
      A threading.Event that will be set when the server has completely stopped.
    """
self._server_lock.acquire()
try:
    if not self._server_started:
        raise ValueError("Server has not started running")
    if self._stop_requested:
        raise ValueError("Server has already stopped")

    self._stop_requested = True
    exit(self.server.stop(grace=grace))
finally:
    self._server_lock.release()
