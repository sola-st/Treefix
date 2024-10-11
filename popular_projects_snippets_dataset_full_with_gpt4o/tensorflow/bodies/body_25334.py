# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui_test.py
self._height = height
self._width = width

self._command_sequence = command_sequence
self._command_counter = 0

# The mock class has no actual textbox. So use this variable to keep
# track of what's entered in the textbox on creation.
self._curr_existing_command = ""

# Observers for test.
# Observers of screen output.
self.unwrapped_outputs = []
self.wrapped_outputs = []
self.scroll_messages = []
self.output_array_pointer_indices = []

self.output_pad_rows = []

# Observers of command textbox.
self.existing_commands = []

# Observer for tab-completion candidates.
self.candidates_lists = []

# Observer for the main menu.
self.main_menu_list = []

# Observer for toast messages.
self.toasts = []

curses_ui.CursesUI.__init__(
    self,
    config=cli_config.CLIConfig(
        config_file_path=os.path.join(tempfile.mkdtemp(), ".tfdbg_config")))

# Override the default path to the command history file to avoid test
# concurrency issues.
_, history_file_path = tempfile.mkstemp()  # safe to ignore fd
self._command_history_store = debugger_cli_common.CommandHistory(
    history_file_path=history_file_path)
