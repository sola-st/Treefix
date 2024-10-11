# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/local_cli_wrapper.py
"""Constructor of LocalCLIDebugWrapperSession.

    Args:
      sess: The TensorFlow `Session` object being wrapped.
      dump_root: (`str`) optional path to the dump root directory. Must be a
        directory that does not exist or an empty directory. If the directory
        does not exist, it will be created by the debugger core during debug
        `run()` calls and removed afterwards. If `None`, the debug dumps will
        be at tfdbg_<random_string> under the system temp directory.
      log_usage: (`bool`) whether the usage of this class is to be logged.
      ui_type: (`str`) requested UI type. Currently supported:
        (curses | readline)
      thread_name_filter: Regular-expression white list for thread name. See
        the doc of `BaseDebugWrapperSession` for details.
      config_file_path: Optional override to the default configuration file
        path, which is at `${HOME}/.tfdbg_config`.

    Raises:
      ValueError: If dump_root is an existing and non-empty directory or if
        dump_root is a file.
    """

if log_usage:
    pass  # No logging for open-source.

framework.BaseDebugWrapperSession.__init__(
    self, sess, thread_name_filter=thread_name_filter)

if not dump_root:
    self._dump_root = tempfile.mkdtemp(prefix=_DUMP_ROOT_PREFIX)
else:
    dump_root = os.path.expanduser(dump_root)
    if os.path.isfile(dump_root):
        raise ValueError("dump_root path points to a file: %s" % dump_root)
    elif os.path.isdir(dump_root) and os.listdir(dump_root):
        raise ValueError("dump_root path points to a non-empty directory: %s" %
                         dump_root)

    self._dump_root = dump_root

self._initialize_argparsers()

# Registered tensor filters.
self._tensor_filters = {}
# Register frequently-used filter(s).
self.add_tensor_filter("has_inf_or_nan", debug_data.has_inf_or_nan)

# Below are the state variables of this wrapper object.
# _active_tensor_filter: what (if any) tensor filter is in effect. If such
#   a filter is in effect, this object will call run() method of the
#   underlying TensorFlow Session object until the filter passes. This is
#   activated by the "-f" flag of the "run" command.
# _run_through_times: keeps track of how many times the wrapper needs to
#   run through without stopping at the run-end CLI. It is activated by the
#   "-t" option of the "run" command.
# _skip_debug: keeps track of whether the current run should be executed
#   without debugging. It is activated by the "-n" option of the "run"
#   command.
#
# _run_start_response: keeps track what OnRunStartResponse the wrapper
#   should return at the next run-start callback. If this information is
#   unavailable (i.e., is None), the run-start CLI will be launched to ask
#   the user. This is the case, e.g., right before the first run starts.
self._active_tensor_filter = None
self._active_filter_exclude_node_names = None
self._active_tensor_filter_run_start_response = None
self._run_through_times = 1
self._skip_debug = False
self._run_start_response = None
self._is_run_start = True
self._ui_type = ui_type
self._config = None
if config_file_path:
    self._config = cli_config.CLIConfig(config_file_path=config_file_path)
