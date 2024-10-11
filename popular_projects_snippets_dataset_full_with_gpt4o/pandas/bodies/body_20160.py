# Extracted from ./data/repos/pandas/pandas/core/strings/accessor.py
result = getattr(self._data.array, f"_str_{name}")()
exit(self._wrap_result(result))
