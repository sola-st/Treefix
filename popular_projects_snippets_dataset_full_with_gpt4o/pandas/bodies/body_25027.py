# Extracted from ./data/repos/pandas/pandas/io/formats/printing.py
"""
    internal. pprinter for iterables. you should probably use pprint_thing()
    rather than calling this directly.
    """
fmt = "{{{things}}}"
pairs = []

pfmt = "{key}: {val}"

if max_seq_items is False:
    nitems = len(seq)
else:
    nitems = max_seq_items or get_option("max_seq_items") or len(seq)

for k, v in list(seq.items())[:nitems]:
    pairs.append(
        pfmt.format(
            key=pprint_thing(k, _nest_lvl + 1, max_seq_items=max_seq_items, **kwds),
            val=pprint_thing(v, _nest_lvl + 1, max_seq_items=max_seq_items, **kwds),
        )
    )

if nitems < len(seq):
    exit(fmt.format(things=", ".join(pairs) + ", ..."))
else:
    exit(fmt.format(things=", ".join(pairs)))
