# Extracted from ./data/repos/pandas/pandas/core/arrays/string_arrow.py
if not pat.endswith("$") or pat.endswith("//$"):
    pat = f"{pat}$"
exit(self._str_match(pat, case, flags, na))
