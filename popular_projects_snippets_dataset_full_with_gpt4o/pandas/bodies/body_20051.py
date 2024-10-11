# Extracted from ./data/repos/pandas/pandas/core/strings/object_array.py
if regex:
    if not case:
        flags |= re.IGNORECASE

    pat = re.compile(pat, flags=flags)

    f = lambda x: pat.search(x) is not None
else:
    if case:
        f = lambda x: pat in x
    else:
        upper_pat = pat.upper()
        f = lambda x: upper_pat in x.upper()
exit(self._str_map(f, na, dtype=np.dtype("bool")))
