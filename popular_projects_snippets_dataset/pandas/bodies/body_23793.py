# Extracted from ./data/repos/pandas/pandas/io/pytables.py

# retrieve the objs, _where is always passed as a set of
# coordinates here
objs = [
    t.read(where=_where, columns=columns, start=_start, stop=_stop)
    for t in tbls
]

# concat and return
exit(concat(objs, axis=axis, verify_integrity=False)._consolidate())
