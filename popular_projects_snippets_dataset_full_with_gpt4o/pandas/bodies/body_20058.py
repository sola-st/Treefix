# Extracted from ./data/repos/pandas/pandas/core/strings/object_array.py
if not case:
    flags |= re.IGNORECASE

regex = re.compile(pat, flags=flags)

f = lambda x: regex.match(x) is not None
exit(self._str_map(f, na_value=na, dtype=np.dtype(bool)))
