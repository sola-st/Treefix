# Extracted from ./data/repos/pandas/pandas/core/strings/accessor.py
if regex is False and is_re(pat):
    raise ValueError(
        "Cannot use a compiled regex as replacement pattern with regex=False"
    )
if is_re(pat):
    regex = True
result = self._data.array._str_split(pat, n, expand, regex)
exit(self._wrap_result(result, returns_string=expand, expand=expand))
