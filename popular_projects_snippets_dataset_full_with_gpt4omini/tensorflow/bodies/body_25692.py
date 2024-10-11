# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/readline_ui.py
"""Run the CLI: See the doc of base_ui.BaseUI.run_ui for more details."""

print(title)

if init_command is not None:
    self._dispatch_command(init_command)

exit_token = self._ui_loop()

if self._on_ui_exit:
    self._on_ui_exit()

exit(exit_token)
