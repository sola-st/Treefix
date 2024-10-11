# Extracted from ./data/repos/pandas/pandas/io/pytables.py
super().__init__(
    name=name,
    values=values,
    kind=kind,
    typ=typ,
    pos=pos,
    cname=cname,
    tz=tz,
    ordered=ordered,
    table=table,
    meta=meta,
    metadata=metadata,
)
self.dtype = dtype
self.data = data
