# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/dumping_wrapper.py
"""Constructor of DumpingDebugWrapperSession.

    Args:
      sess: The TensorFlow `Session` object being wrapped.
      session_root: (`str`) Path to the session root directory. Must be a
        directory that does not exist or an empty directory. If the directory
        does not exist, it will be created by the debugger core during debug
        `tf.Session.run`
        calls.
        As the `run()` calls occur, subdirectories will be added to
        `session_root`. The subdirectories' names has the following pattern:
          run_<epoch_time_stamp>_<zero_based_run_counter>
        E.g., run_1480734393835964_ad4c953a85444900ae79fc1b652fb324
      watch_fn: (`Callable`) A Callable that can be used to define per-run
        debug ops and watched tensors. See the doc of
        `NonInteractiveDebugWrapperSession.__init__()` for details.
      thread_name_filter: Regular-expression white list for threads on which the
        wrapper session will be active. See doc of `BaseDebugWrapperSession` for
        more details.
      pass_through_operrors: If true, all captured OpErrors will be
        propagated. By default this captures all OpErrors.
      log_usage: (`bool`) whether the usage of this class is to be logged.

    Raises:
       ValueError: If `session_root` is an existing and non-empty directory or
       if `session_root` is a file.
    """

if log_usage:
    pass  # No logging for open-source.

framework.NonInteractiveDebugWrapperSession.__init__(
    self, sess, watch_fn=watch_fn, thread_name_filter=thread_name_filter,
    pass_through_operrors=pass_through_operrors)

session_root = os.path.expanduser(session_root)
if gfile.Exists(session_root):
    if not gfile.IsDirectory(session_root):
        raise ValueError(
            "session_root path points to a file: %s" % session_root)
    elif gfile.ListDirectory(session_root):
        raise ValueError(
            "session_root path points to a non-empty directory: %s" %
            session_root)
else:
    gfile.MakeDirs(session_root)
self._session_root = session_root

self._run_counter = 0
self._run_counter_lock = threading.Lock()
