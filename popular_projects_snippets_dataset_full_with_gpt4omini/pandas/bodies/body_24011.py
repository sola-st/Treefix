# Extracted from ./data/repos/pandas/pandas/io/json/_json.py
"""
        Adds a `schema` attribute with the Table Schema, resets
        the index (can't do in caller, because the schema inference needs
        to know what the index is, forces orient to records, and forces
        date_format to 'iso'.
        """
super().__init__(
    obj,
    orient,
    date_format,
    double_precision,
    ensure_ascii,
    date_unit,
    index,
    default_handler=default_handler,
    indent=indent,
)

if date_format != "iso":
    msg = (
        "Trying to write with `orient='table'` and "
        f"`date_format='{date_format}'`. Table Schema requires dates "
        "to be formatted with `date_format='iso'`"
    )
    raise ValueError(msg)

self.schema = build_table_schema(obj, index=self.index)

# NotImplemented on a column MultiIndex
if obj.ndim == 2 and isinstance(obj.columns, MultiIndex):
    raise NotImplementedError(
        "orient='table' is not supported for MultiIndex columns"
    )

# TODO: Do this timedelta properly in objToJSON.c See GH #15137
if (
    (obj.ndim == 1)
    and (obj.name in set(obj.index.names))
    or len(obj.columns.intersection(obj.index.names))
):
    msg = "Overlapping names between the index and columns"
    raise ValueError(msg)

obj = obj.copy()
timedeltas = obj.select_dtypes(include=["timedelta"]).columns
if len(timedeltas):
    obj[timedeltas] = obj[timedeltas].applymap(lambda x: x.isoformat())
# Convert PeriodIndex to datetimes before serializing
if is_period_dtype(obj.index.dtype):
    obj.index = obj.index.to_timestamp()

# exclude index from obj if index=False
if not self.index:
    self.obj = obj.reset_index(drop=True)
else:
    self.obj = obj.reset_index(drop=False)
self.date_format = "iso"
self.orient = "records"
self.index = index
