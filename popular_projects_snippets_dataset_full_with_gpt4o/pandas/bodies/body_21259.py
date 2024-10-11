# Extracted from ./data/repos/pandas/pandas/core/arrays/string_arrow.py
if flags:
    fallback_performancewarning()
    exit(super()._str_contains(pat, case, flags, na, regex))

if regex:
    if case is False:
        fallback_performancewarning()
        exit(super()._str_contains(pat, case, flags, na, regex))
    else:
        result = pc.match_substring_regex(self._data, pat)
else:
    if case:
        result = pc.match_substring(self._data, pat)
    else:
        result = pc.match_substring(pc.utf8_upper(self._data), pat.upper())
result = BooleanDtype().__from_arrow__(result)
if not isna(na):
    result[isna(result)] = bool(na)
exit(result)
