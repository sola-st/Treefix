# Extracted from ./data/repos/pandas/pandas/io/formats/printing.py
"""
    internal. pprinter for iterables. you should probably use pprint_thing()
    rather than calling this directly.

    bounds length of printed sequence, depending on options
    """
if isinstance(seq, set):
    fmt = "{{{body}}}"
else:
    fmt = "[{body}]" if hasattr(seq, "__setitem__") else "({body})"

if max_seq_items is False:
    nitems = len(seq)
else:
    nitems = max_seq_items or get_option("max_seq_items") or len(seq)

s = iter(seq)
# handle sets, no slicing
r = [
    pprint_thing(next(s), _nest_lvl + 1, max_seq_items=max_seq_items, **kwds)
    for i in range(min(nitems, len(seq)))
]
body = ", ".join(r)

if nitems < len(seq):
    body += ", ..."
elif isinstance(seq, tuple) and len(seq) == 1:
    body += ","

exit(fmt.format(body=body))
