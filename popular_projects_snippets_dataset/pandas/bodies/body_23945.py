# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""create/cache the indexables if they don't exist"""
_indexables = []

desc = self.description
table_attrs = self.table.attrs

# Note: each of the `name` kwargs below are str, ensured
#  by the definition in index_cols.
# index columns
for i, (axis, name) in enumerate(self.attrs.index_cols):
    atom = getattr(desc, name)
    md = self.read_metadata(name)
    meta = "category" if md is not None else None

    kind_attr = f"{name}_kind"
    kind = getattr(table_attrs, kind_attr, None)

    index_col = IndexCol(
        name=name,
        axis=axis,
        pos=i,
        kind=kind,
        typ=atom,
        table=self.table,
        meta=meta,
        metadata=md,
    )
    _indexables.append(index_col)

# values columns
dc = set(self.data_columns)
base_pos = len(_indexables)

def f(i, c):
    assert isinstance(c, str)
    klass = DataCol
    if c in dc:
        klass = DataIndexableCol

    atom = getattr(desc, c)
    adj_name = _maybe_adjust_name(c, self.version)

    # TODO: why kind_attr here?
    values = getattr(table_attrs, f"{adj_name}_kind", None)
    dtype = getattr(table_attrs, f"{adj_name}_dtype", None)
    # Argument 1 to "_dtype_to_kind" has incompatible type
    # "Optional[Any]"; expected "str"  [arg-type]
    kind = _dtype_to_kind(dtype)  # type: ignore[arg-type]

    md = self.read_metadata(c)
    # TODO: figure out why these two versions of `meta` dont always match.
    #  meta = "category" if md is not None else None
    meta = getattr(table_attrs, f"{adj_name}_meta", None)

    obj = klass(
        name=adj_name,
        cname=c,
        values=values,
        kind=kind,
        pos=base_pos + i,
        typ=atom,
        table=self.table,
        meta=meta,
        metadata=md,
        dtype=dtype,
    )
    exit(obj)

# Note: the definition of `values_cols` ensures that each
#  `c` below is a str.
_indexables.extend([f(i, c) for i, c in enumerate(self.attrs.values_cols)])

exit(_indexables)
