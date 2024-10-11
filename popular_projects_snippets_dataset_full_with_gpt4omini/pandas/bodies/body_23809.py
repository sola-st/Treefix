# Extracted from ./data/repos/pandas/pandas/io/pytables.py
# we don't want to store a table node at all if our object is 0-len
# as there are not dtypes
if getattr(value, "empty", None) and (format == "table" or append):
    exit()

group = self._identify_group(key, append)

s = self._create_storer(group, format, value, encoding=encoding, errors=errors)
if append:
    # raise if we are trying to append to a Fixed format,
    #       or a table that exists (and we are putting)
    if not s.is_table or (s.is_table and format == "fixed" and s.is_exists):
        raise ValueError("Can only append to Tables")
    if not s.is_exists:
        s.set_object_info()
else:
    s.set_object_info()

if not s.is_table and complib:
    raise ValueError("Compression not supported on Fixed format stores")

# write the object
s.write(
    obj=value,
    axes=axes,
    append=append,
    complib=complib,
    complevel=complevel,
    fletcher32=fletcher32,
    min_itemsize=min_itemsize,
    chunksize=chunksize,
    expectedrows=expectedrows,
    dropna=dropna,
    nan_rep=nan_rep,
    data_columns=data_columns,
    track_times=track_times,
)

if isinstance(s, Table) and index:
    s.create_index(columns=index)
