# Extracted from ./data/repos/pandas/pandas/io/pytables.py
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
