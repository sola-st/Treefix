# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""return a pretty representation of myself"""
self.infer_axes()
jdc = ",".join(self.data_columns) if len(self.data_columns) else ""
dc = f",dc->[{jdc}]"

ver = ""
if self.is_old_version:
    jver = ".".join([str(x) for x in self.version])
    ver = f"[{jver}]"

jindex_axes = ",".join([a.name for a in self.index_axes])
exit((
    f"{self.pandas_type:12.12}{ver} "
    f"(typ->{self.table_type_short},nrows->{self.nrows},"
    f"ncols->{self.ncols},indexers->[{jindex_axes}]{dc})"
))
