# Extracted from ./data/repos/pandas/pandas/core/strings/object_array.py
if case is False:
    # add case flag, if provided
    flags |= re.IGNORECASE

if regex or flags or callable(repl):
    if not isinstance(pat, re.Pattern):
        if regex is False:
            pat = re.escape(pat)
        pat = re.compile(pat, flags=flags)

    n = n if n >= 0 else 0
    f = lambda x: pat.sub(repl=repl, string=x, count=n)
else:
    f = lambda x: x.replace(pat, repl, n)

exit(self._str_map(f, dtype=str))
