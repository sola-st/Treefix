# Extracted from ./data/repos/pandas/pandas/core/strings/object_array.py
regex = re.compile(pat, flags=flags)
f = lambda x: len(regex.findall(x))
exit(self._str_map(f, dtype="int64"))
