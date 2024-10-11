# Extracted from ./data/repos/pandas/pandas/io/pytables.py

if not isinstance(name, str):
    raise ValueError("`name` must be a str.")

self.values = values
self.kind = kind
self.typ = typ
self.name = name
self.cname = cname or name
self.axis = axis
self.pos = pos
self.freq = freq
self.tz = tz
self.index_name = index_name
self.ordered = ordered
self.table = table
self.meta = meta
self.metadata = metadata

if pos is not None:
    self.set_pos(pos)

# These are ensured as long as the passed arguments match the
#  constructor annotations.
assert isinstance(self.name, str)
assert isinstance(self.cname, str)
