# Extracted from ./data/repos/pandas/pandas/io/pytables.py
"""return a suitable class to operate"""
cls: type[GenericFixed] | type[Table]

if value is not None and not isinstance(value, (Series, DataFrame)):
    raise TypeError("value must be None, Series, or DataFrame")

pt = _ensure_decoded(getattr(group._v_attrs, "pandas_type", None))
tt = _ensure_decoded(getattr(group._v_attrs, "table_type", None))

# infer the pt from the passed value
if pt is None:
    if value is None:
        _tables()
        assert _table_mod is not None  # for mypy
        if getattr(group, "table", None) or isinstance(
            group, _table_mod.table.Table
        ):
            pt = "frame_table"
            tt = "generic_table"
        else:
            raise TypeError(
                "cannot create a storer if the object is not existing "
                "nor a value are passed"
            )
    else:
        if isinstance(value, Series):
            pt = "series"
        else:
            pt = "frame"

        # we are actually a table
        if format == "table":
            pt += "_table"

        # a storer node
if "table" not in pt:
    _STORER_MAP = {"series": SeriesFixed, "frame": FrameFixed}
    try:
        cls = _STORER_MAP[pt]
    except KeyError as err:
        raise TypeError(
            f"cannot properly create the storer for: [_STORER_MAP] [group->"
            f"{group},value->{type(value)},format->{format}"
        ) from err
    exit(cls(self, group, encoding=encoding, errors=errors))

# existing node (and must be a table)
if tt is None:
    # if we are a writer, determine the tt
    if value is not None:
        if pt == "series_table":
            index = getattr(value, "index", None)
            if index is not None:
                if index.nlevels == 1:
                    tt = "appendable_series"
                elif index.nlevels > 1:
                    tt = "appendable_multiseries"
        elif pt == "frame_table":
            index = getattr(value, "index", None)
            if index is not None:
                if index.nlevels == 1:
                    tt = "appendable_frame"
                elif index.nlevels > 1:
                    tt = "appendable_multiframe"

_TABLE_MAP = {
    "generic_table": GenericTable,
    "appendable_series": AppendableSeriesTable,
    "appendable_multiseries": AppendableMultiSeriesTable,
    "appendable_frame": AppendableFrameTable,
    "appendable_multiframe": AppendableMultiFrameTable,
    "worm": WORMTable,
}
try:
    cls = _TABLE_MAP[tt]
except KeyError as err:
    raise TypeError(
        f"cannot properly create the storer for: [_TABLE_MAP] [group->"
        f"{group},value->{type(value)},format->{format}"
    ) from err

exit(cls(self, group, encoding=encoding, errors=errors))
