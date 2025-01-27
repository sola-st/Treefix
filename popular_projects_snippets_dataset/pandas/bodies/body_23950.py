# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""
        Create and return the axes.

        Parameters
        ----------
        axes: list or None
            The names or numbers of the axes to create.
        obj : DataFrame
            The object to create axes on.
        validate: bool, default True
            Whether to validate the obj against an existing object already written.
        nan_rep :
            A value to use for string column nan_rep.
        data_columns : List[str], True, or None, default None
            Specify the columns that we want to create to allow indexing on.

            * True : Use all available columns.
            * None : Use no columns.
            * List[str] : Use the specified columns.

        min_itemsize: Dict[str, int] or None, default None
            The min itemsize for a column in bytes.
        """
if not isinstance(obj, DataFrame):
    group = self.group._v_name
    raise TypeError(
        f"cannot properly create the storer for: [group->{group},"
        f"value->{type(obj)}]"
    )

# set the default axes if needed
if axes is None:
    axes = [0]

# map axes to numbers
axes = [obj._get_axis_number(a) for a in axes]

# do we have an existing table (if so, use its axes & data_columns)
if self.infer_axes():
    table_exists = True
    axes = [a.axis for a in self.index_axes]
    data_columns = list(self.data_columns)
    nan_rep = self.nan_rep
    # TODO: do we always have validate=True here?
else:
    table_exists = False

new_info = self.info

assert self.ndim == 2  # with next check, we must have len(axes) == 1
# currently support on ndim-1 axes
if len(axes) != self.ndim - 1:
    raise ValueError(
        "currently only support ndim-1 indexers in an AppendableTable"
    )

# create according to the new data
new_non_index_axes: list = []

# nan_representation
if nan_rep is None:
    nan_rep = "nan"

# We construct the non-index-axis first, since that alters new_info
idx = [x for x in [0, 1] if x not in axes][0]

a = obj.axes[idx]
# we might be able to change the axes on the appending data if necessary
append_axis = list(a)
if table_exists:
    indexer = len(new_non_index_axes)  # i.e. 0
    exist_axis = self.non_index_axes[indexer][1]
    if not array_equivalent(np.array(append_axis), np.array(exist_axis)):

        # ahah! -> reindex
        if array_equivalent(
            np.array(sorted(append_axis)), np.array(sorted(exist_axis))
        ):
            append_axis = exist_axis

        # the non_index_axes info
info = new_info.setdefault(idx, {})
info["names"] = list(a.names)
info["type"] = type(a).__name__

new_non_index_axes.append((idx, append_axis))

# Now we can construct our new index axis
idx = axes[0]
a = obj.axes[idx]
axis_name = obj._get_axis_name(idx)
new_index = _convert_index(axis_name, a, self.encoding, self.errors)
new_index.axis = idx

# Because we are always 2D, there is only one new_index, so
#  we know it will have pos=0
new_index.set_pos(0)
new_index.update_info(new_info)
new_index.maybe_set_size(min_itemsize)  # check for column conflicts

new_index_axes = [new_index]
j = len(new_index_axes)  # i.e. 1
assert j == 1

# reindex by our non_index_axes & compute data_columns
assert len(new_non_index_axes) == 1
for a in new_non_index_axes:
    obj = _reindex_axis(obj, a[0], a[1])

transposed = new_index.axis == 1

# figure out data_columns and get out blocks
data_columns = self.validate_data_columns(
    data_columns, min_itemsize, new_non_index_axes
)

frame = self.get_object(obj, transposed)._consolidate()

blocks, blk_items = self._get_blocks_and_items(
    frame, table_exists, new_non_index_axes, self.values_axes, data_columns
)

# add my values
vaxes = []
for i, (blk, b_items) in enumerate(zip(blocks, blk_items)):

    # shape of the data column are the indexable axes
    klass = DataCol
    name = None

    # we have a data_column
    if data_columns and len(b_items) == 1 and b_items[0] in data_columns:
        klass = DataIndexableCol
        name = b_items[0]
        if not (name is None or isinstance(name, str)):
            # TODO: should the message here be more specifically non-str?
            raise ValueError("cannot have non-object label DataIndexableCol")

            # make sure that we match up the existing columns
            # if we have an existing table
    existing_col: DataCol | None

    if table_exists and validate:
        try:
            existing_col = self.values_axes[i]
        except (IndexError, KeyError) as err:
            raise ValueError(
                f"Incompatible appended table [{blocks}]"
                f"with existing table [{self.values_axes}]"
            ) from err
    else:
        existing_col = None

    new_name = name or f"values_block_{i}"
    data_converted = _maybe_convert_for_string_atom(
        new_name,
        blk.values,
        existing_col=existing_col,
        min_itemsize=min_itemsize,
        nan_rep=nan_rep,
        encoding=self.encoding,
        errors=self.errors,
        columns=b_items,
    )
    adj_name = _maybe_adjust_name(new_name, self.version)

    typ = klass._get_atom(data_converted)
    kind = _dtype_to_kind(data_converted.dtype.name)
    tz = None
    if getattr(data_converted, "tz", None) is not None:
        tz = _get_tz(data_converted.tz)

    meta = metadata = ordered = None
    if is_categorical_dtype(data_converted.dtype):
        ordered = data_converted.ordered
        meta = "category"
        metadata = np.array(data_converted.categories, copy=False).ravel()

    data, dtype_name = _get_data_and_dtype_name(data_converted)

    col = klass(
        name=adj_name,
        cname=new_name,
        values=list(b_items),
        typ=typ,
        pos=j,
        kind=kind,
        tz=tz,
        ordered=ordered,
        meta=meta,
        metadata=metadata,
        dtype=dtype_name,
        data=data,
    )
    col.update_info(new_info)

    vaxes.append(col)

    j += 1

dcs = [col.name for col in vaxes if col.is_data_indexable]

new_table = type(self)(
    parent=self.parent,
    group=self.group,
    encoding=self.encoding,
    errors=self.errors,
    index_axes=new_index_axes,
    non_index_axes=new_non_index_axes,
    values_axes=vaxes,
    data_columns=dcs,
    info=new_info,
    nan_rep=nan_rep,
)
if hasattr(self, "levels"):
    # TODO: get this into constructor, only for appropriate subclass
    new_table.levels = self.levels

new_table.validate_min_itemsize(min_itemsize)

if validate and table_exists:
    new_table.validate(self)

exit(new_table)
