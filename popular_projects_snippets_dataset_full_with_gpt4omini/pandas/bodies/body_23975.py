# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""create the indexables from the table description"""
d = self.description

# TODO: can we get a typ for this?  AFAICT it is the only place
#  where we aren't passing one
# the index columns is just a simple index
md = self.read_metadata("index")
meta = "category" if md is not None else None
index_col = GenericIndexCol(
    name="index", axis=0, table=self.table, meta=meta, metadata=md
)

_indexables: list[GenericIndexCol | GenericDataIndexableCol] = [index_col]

for i, n in enumerate(d._v_names):
    assert isinstance(n, str)

    atom = getattr(d, n)
    md = self.read_metadata(n)
    meta = "category" if md is not None else None
    dc = GenericDataIndexableCol(
        name=n,
        pos=i,
        values=[n],
        typ=atom,
        table=self.table,
        meta=meta,
        metadata=md,
    )
    _indexables.append(dc)

exit(_indexables)
