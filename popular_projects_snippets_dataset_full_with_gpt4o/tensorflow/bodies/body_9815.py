# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session.py
if exec_type is errors.OpError:
    logging.error('Session closing due to OpError: %s', (exec_value,))
try:
    self._default_session_context_manager.__exit__(exec_type, exec_value,
                                                   exec_tb)
except RuntimeError as error:
    if error == exec_value:
        # NOTE(skyewm): for some reason, in Python3,
        # _default_session_context_manager.__exit__ will re-raise the "not
        # re-entrant" exception raised in __enter__ above (note that if we're
        # here, we're in the outer session context manager, since __exit__ is
        # not called when __enter__ raises an exception). We still want to
        # continue cleaning up this context manager before the exception is
        # further propagated, so we ignore it here (note that it'll continue
        # being propagated after this method completes).
        pass
    else:
        raise
self._default_graph_context_manager.__exit__(exec_type, exec_value, exec_tb)

self._default_session_context_manager = None
self._default_graph_context_manager = None

# If we are closing due to an exception, set a time limit on our Close() to
# avoid blocking forever.
# TODO(b/120204635) remove this when deadlock is fixed.
if exec_type:
    close_thread = threading.Thread(
        name='SessionCloseThread', target=self.close)
    close_thread.daemon = True
    close_thread.start()
    close_thread.join(30.0)
    if close_thread.is_alive():
        logging.error(
            'Session failed to close after 30 seconds. Continuing after this '
            'point may leave your program in an undefined state.')
else:
    self.close()
