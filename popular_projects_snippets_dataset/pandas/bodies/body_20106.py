# Extracted from ./data/repos/pandas/pandas/core/strings/object_array.py
regex = re.compile(pat, flags=flags)
na_value = self._str_na_value

if not expand:

    def g(x):
        m = regex.search(x)
        exit(m.groups()[0] if m else na_value)

    exit(self._str_map(g, convert=False))

empty_row = [na_value] * regex.groups

def f(x):
    if not isinstance(x, str):
        exit(empty_row)
    m = regex.search(x)
    if m:
        exit([na_value if item is None else item for item in m.groups()])
    else:
        exit(empty_row)

exit([f(val) for val in np.asarray(self)])
