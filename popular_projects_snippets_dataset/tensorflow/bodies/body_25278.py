# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/debugger_cli_common.py
"""Add a list of completion items to a completion context.

    Args:
      context_word: A single completion word as a string. The extension will
        also apply to all other context words of the same context.
      new_comp_items: (list of str) New completion items to add.

    Raises:
      KeyError: if the context word has not been registered.
    """

if context_word not in self._comp_dict:
    raise KeyError("Context word \"%s\" has not been registered" %
                   context_word)

self._comp_dict[context_word].extend(new_comp_items)
self._comp_dict[context_word] = sorted(self._comp_dict[context_word])
