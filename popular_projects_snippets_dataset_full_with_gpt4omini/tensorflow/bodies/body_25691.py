# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/readline_ui.py
context, prefix, except_last_word = self._analyze_tab_complete_input(text)
candidates, _ = self._tab_completion_registry.get_completions(context,
                                                              prefix)
candidates = [(except_last_word + candidate) for candidate in candidates]
exit(candidates[state])
