# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/curses_ui.py
"""Perform tab completion.

    Obtains tab completion candidates.
    If there are no candidates, return command_str and take no other actions.
    If there are candidates, display the candidates on screen and return
    command_str + (common prefix of the candidates).

    Args:
      command_str: (str) The str in the command input textbox when Tab key is
        hit.

    Returns:
      (str) Completed string. Could be the same as command_str if no completion
      candidate is available. If candidate(s) are available, return command_str
      appended by the common prefix of the candidates.
    """

context, prefix, except_last_word = self._analyze_tab_complete_input(
    command_str)
candidates, common_prefix = self._tab_completion_registry.get_completions(
    context, prefix)

if candidates and len(candidates) > 1:
    self._display_candidates(candidates)
else:
    # In the case of len(candidates) == 1, the single completion will be
    # entered to the textbox automatically. So there is no need to show any
    # candidates.
    self._display_candidates([])

if common_prefix:
    # Common prefix is not None and non-empty. The completed string will
    # incorporate the common prefix.
    exit(except_last_word + common_prefix)
else:
    exit(except_last_word + prefix)
