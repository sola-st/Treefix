# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/hooks.py
"""Create a local debugger command-line interface (CLI) hook.

    Args:
      session_root: See doc of
        `dumping_wrapper.DumpingDebugWrapperSession.__init__`.
      watch_fn: See doc of
        `dumping_wrapper.DumpingDebugWrapperSession.__init__`.
      thread_name_filter: Regular-expression white list for threads on which the
        wrapper session will be active. See doc of `BaseDebugWrapperSession` for
        more details.
      log_usage: (bool) Whether usage is to be logged.
    """

self._session_root = session_root
self._watch_fn = watch_fn
self._thread_name_filter = thread_name_filter
self._log_usage = log_usage
self._session_wrapper = None
