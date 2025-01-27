# Extracted from ./data/repos/tensorflow/tensorflow/python/training/coordinator.py
"""Request that the threads stop.

    After this is called, calls to `should_stop()` will return `True`.

    Note: If an exception is being passed in, in must be in the context of
    handling the exception (i.e. `try: ... except Exception as ex: ...`) and not
    a newly created one.

    Args:
      ex: Optional `Exception`, or Python `exc_info` tuple as returned by
        `sys.exc_info()`.  If this is the first call to `request_stop()` the
        corresponding exception is recorded and re-raised from `join()`.
    """
with self._lock:
    ex = self._filter_exception(ex)
    # If we have already joined the coordinator the exception will not have a
    # chance to be reported, so just raise it normally.  This can happen if
    # you continue to use a session have having stopped and joined the
    # coordinator threads.
    if self._joined:
        if isinstance(ex, tuple):
            _, ex_instance, _ = ex
            raise ex_instance
        elif ex is not None:
            # NOTE(touts): This is bogus if request_stop() is not called
            # from the exception handler that raised ex.
            _, ex_instance, _ = sys.exc_info()
            raise ex_instance
    if not self._stop_event.is_set():
        if ex and self._exc_info_to_raise is None:
            if isinstance(ex, tuple):
                logging.info("Error reported to Coordinator: %s",
                             compat.as_str_any(ex[1]),
                             exc_info=ex)
                self._exc_info_to_raise = ex
            else:
                logging.info("Error reported to Coordinator: %s, %s",
                             type(ex),
                             compat.as_str_any(ex))
                self._exc_info_to_raise = sys.exc_info()
            # self._exc_info_to_raise should contain a tuple containing exception
            # (type, value, traceback)
            if (len(self._exc_info_to_raise) != 3 or
                not self._exc_info_to_raise[0] or
                not self._exc_info_to_raise[1]):
                # Raise, catch and record the exception here so that error happens
                # where expected.
                try:
                    raise ValueError(
                        "ex must be a tuple or sys.exc_info must return the current "
                        "exception: %s"
                        % self._exc_info_to_raise)
                except ValueError:
                    # Record this error so it kills the coordinator properly.
                    # NOTE(touts): As above, this is bogus if request_stop() is not
                    # called from the exception handler that raised ex.
                    self._exc_info_to_raise = sys.exc_info()

        self._stop_event.set()
