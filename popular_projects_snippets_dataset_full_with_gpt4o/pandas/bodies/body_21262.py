# Extracted from ./data/repos/pandas/pandas/core/arrays/string_arrow.py
if isinstance(pat, re.Pattern) or callable(repl) or not case or flags:
    fallback_performancewarning()
    exit(super()._str_replace(pat, repl, n, case, flags, regex))

func = pc.replace_substring_regex if regex else pc.replace_substring
result = func(self._data, pattern=pat, replacement=repl, max_replacements=n)
exit(type(self)(result))
