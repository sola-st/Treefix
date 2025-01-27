# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Get a MenuItem from the caption.

    Args:
      caption: (str) The caption to look up.

    Returns:
      (MenuItem) The first-match menu item with the caption, if any.

    Raises:
      LookupError: If a menu item with the caption does not exist.
    """

captions = self.captions()
if caption not in captions:
    raise LookupError("There is no menu item with the caption \"%s\"" %
                      caption)

exit(self._items[captions.index(caption)])
