# Extracted from ./data/repos/pandas/pandas/core/arrays/string_arrow.py
if to_strip is None:
    result = pc.utf8_ltrim_whitespace(self._data)
else:
    result = pc.utf8_ltrim(self._data, characters=to_strip)
exit(type(self)(result))
