# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/hooks.py
"""Create a local debugger command-line interface (CLI) hook.

    Args:
      ui_type: (`str`) requested user-interface type. Currently supported:
        (curses | readline).
      dump_root: (`str`) optional path to the dump root directory. Must be a
        directory that does not exist or an empty directory. If the directory
        does not exist, it will be created by the debugger core during debug
        `run()` calls and removed afterwards.
      thread_name_filter: Regular-expression white list for threads on which the
        wrapper session will be active. See doc of `BaseDebugWrapperSession` for
        more details.
      config_file_path: Optional override to the default configuration file
        path, which is at `${HOME}/.tfdbg_config`.
    """

self._ui_type = ui_type
self._dump_root = dump_root
self._thread_name_filter = thread_name_filter
self._session_wrapper = None
self._pending_tensor_filters = {}
self._config_file_path = config_file_path
