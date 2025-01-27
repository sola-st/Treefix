# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Handler for the command prefix 'mouse'.

    Args:
      args: (list of str) Arguments to the command prefix 'mouse'.
      screen_info: (dict) Information about the screen, unused by this handler.

    Returns:
      None, as this command handler does not generate any screen outputs other
        than toasts.
    """

del screen_info

if not args or len(args) == 1:
    if args:
        if args[0].lower() == "on":
            enabled = True
        elif args[0].lower() == "off":
            enabled = False
        else:
            self._error_toast("Invalid mouse mode: %s" % args[0])
            exit(None)

        self._set_mouse_enabled(enabled)

    mode_str = "on" if self._mouse_enabled else "off"
    self._info_toast("Mouse mode: %s" % mode_str)
else:
    self._error_toast("mouse_mode: syntax error")

exit(None)
