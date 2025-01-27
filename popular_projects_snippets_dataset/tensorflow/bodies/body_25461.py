# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Constructor of CursesUI.

    Args:
      on_ui_exit: (Callable) Callback invoked when the UI exits.
      config: An instance of `cli_config.CLIConfig()` carrying user-facing
        configurations.
    """

base_ui.BaseUI.__init__(self, on_ui_exit=on_ui_exit, config=config)

self._screen_init()
self._screen_refresh_size()
# TODO(cais): Error out if the size of the screen is too small.

# Initialize some UI component size and locations.
self._init_layout()

self._command_history_store = debugger_cli_common.CommandHistory()

# Active list of command history, used in history navigation.
# _command_handler_registry holds all the history commands the CLI has
# received, up to a size limit. _active_command_history is the history
# currently being navigated in, e.g., using the Up/Down keys. The latter
# can be different from the former during prefixed or regex-based history
# navigation, e.g., when user enter the beginning of a command and hit Up.
self._active_command_history = []

# Pointer to the current position in the history sequence.
# 0 means it is a new command being keyed in.
self._command_pointer = 0

self._command_history_limit = 100

self._pending_command = ""

self._nav_history = curses_widgets.CursesNavigationHistory(10)

# State related to screen output.
self._output_pad = None
self._output_pad_row = 0
self._output_array_pointer_indices = None
self._curr_unwrapped_output = None
self._curr_wrapped_output = None

try:
    # Register signal handler for SIGINT.
    signal.signal(signal.SIGINT, self._interrupt_handler)
except ValueError:
    # Running in a child thread, can't catch signals.
    pass

self.register_command_handler(
    "mouse",
    self._mouse_mode_command_handler,
    "Get or set the mouse mode of this CLI: (on|off)",
    prefix_aliases=["m"])
