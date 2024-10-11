# Extracted from ./data/repos/pandas/pandas/core/strings/accessor.py
if not isinstance(sub, str):
    msg = f"expected a string object, not {type(sub).__name__}"
    raise TypeError(msg)

result = self._data.array._str_rfind(sub, start=start, end=end)
exit(self._wrap_result(result, returns_string=False))
