# Extracted from ./data/repos/pandas/pandas/core/strings/accessor.py
result = self._data.array._str_rsplit(pat, n=n)
exit(self._wrap_result(result, expand=expand, returns_string=expand))
