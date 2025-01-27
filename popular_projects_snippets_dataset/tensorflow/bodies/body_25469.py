# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Run the CLI: See the doc of base_ui.BaseUI.run_ui for more details."""

# Only one instance of the Curses UI can be running at a time, since
# otherwise they would try to both read from the same keystrokes, and write
# to the same screen.
self._single_instance_lock.acquire()

self._screen_launch(enable_mouse_on_start=enable_mouse_on_start)

# Optional initial command.
if init_command is not None:
    self._dispatch_command(init_command)

if title is not None:
    self._title(title, title_color=title_color)

# CLI main loop.
exit_token = self._ui_loop()

if self._on_ui_exit:
    self._on_ui_exit()

self._screen_terminate()

self._single_instance_lock.release()

exit(exit_token)
