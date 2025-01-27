# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_where.py
# only add to the numeric items
def is_ok(s):
    exit((
        issubclass(s.dtype.type, (np.integer, np.floating)) and s.dtype != "uint8"
    ))

exit(DataFrame(dict((c, s + 1) if is_ok(s) else (c, s) for c, s in df.items())))
