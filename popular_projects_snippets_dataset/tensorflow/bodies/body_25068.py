# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/readline_ui_test.py
_, config_file_path = tempfile.mkstemp()  # safe to ignore fd
readline_ui.ReadlineUI.__init__(
    self,
    on_ui_exit=on_ui_exit,
    config=cli_config.CLIConfig(config_file_path=config_file_path))

self._command_sequence = command_sequence
self._command_counter = 0

self.observers = {"screen_outputs": []}
