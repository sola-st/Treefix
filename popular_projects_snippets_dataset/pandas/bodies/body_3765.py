# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_align.py
left = frame.iloc[0:4, :10]
right = frame.iloc[2:, 6:]
empty = frame.iloc[:0, :0]

self._check_align(left, right, axis=ax, fill_axis=fax, how=kind, method=meth)
self._check_align(
    left, right, axis=ax, fill_axis=fax, how=kind, method=meth, limit=1
)

# empty left
self._check_align(empty, right, axis=ax, fill_axis=fax, how=kind, method=meth)
self._check_align(
    empty, right, axis=ax, fill_axis=fax, how=kind, method=meth, limit=1
)

# empty right
self._check_align(left, empty, axis=ax, fill_axis=fax, how=kind, method=meth)
self._check_align(
    left, empty, axis=ax, fill_axis=fax, how=kind, method=meth, limit=1
)

# both empty
self._check_align(empty, empty, axis=ax, fill_axis=fax, how=kind, method=meth)
self._check_align(
    empty, empty, axis=ax, fill_axis=fax, how=kind, method=meth, limit=1
)
