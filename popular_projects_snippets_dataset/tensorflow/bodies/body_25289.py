# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Menu constructor.

    TODO(cais): Nested menu is currently not supported. Support it.

    Args:
      caption: (str) caption of the menu item.
      content: Content of the menu item. For a menu item that triggers
        a command, for example, content is the command string.
      enabled: (bool) whether this menu item is enabled.
    """

self._caption = caption
self._content = content
self._enabled = enabled
