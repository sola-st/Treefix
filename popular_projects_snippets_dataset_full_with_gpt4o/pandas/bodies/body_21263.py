# Extracted from ./data/repos/pandas/pandas/core/arrays/string_arrow.py
if not pat.startswith("^"):
    pat = f"^{pat}"
exit(self._str_contains(pat, case, flags, na, regex=True))
