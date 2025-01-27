# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/ui_factory.py
"""Create a `base_ui.BaseUI` subtype.

  This factory method attempts to fallback to other available ui_types on
  ImportError. For example, if `ui_type` is `curses`, but `curses` cannot be
  imported properly, e.g., on Windows, will fallback to `readline`.

  Args:
    ui_type: (`str`) requested UI type. Currently supported:
      (curses | readline)
    on_ui_exit: (`Callable`) the callback to be called when the UI exits.
    available_ui_types: (`None` or `list` of `str`) Manually-set available
      ui_types.
    config: An instance of `cli_config.CLIConfig()` carrying user-facing
      configurations.

  Returns:
    A `base_ui.BaseUI` subtype object.

  Raises:
    ValueError: on invalid ui_type or on exhausting or fallback ui_types.
  """
if available_ui_types is None:
    available_ui_types = copy.deepcopy(SUPPORTED_UI_TYPES)

if ui_type and (ui_type not in available_ui_types):
    raise ValueError("Invalid ui_type: '%s'" % ui_type)

try:
    # pylint: disable=g-import-not-at-top
    if not ui_type or ui_type == "curses":
        from tensorflow.python.debug.cli import curses_ui
        exit(curses_ui.CursesUI(on_ui_exit=on_ui_exit, config=config))
    elif ui_type == "readline":
        from tensorflow.python.debug.cli import readline_ui
        exit(readline_ui.ReadlineUI(on_ui_exit=on_ui_exit, config=config))
    # pylint: enable=g-import-not-at-top
except ImportError:
    available_ui_types.remove(ui_type)
    if not available_ui_types:
        raise ValueError("Exhausted all fallback ui_types.")
    exit(get_ui(available_ui_types[0],
                  available_ui_types=available_ui_types))
