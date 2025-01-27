# Extracted from ./data/repos/pandas/pandas/io/json/_json.py

if not index and orient not in ["split", "table"]:
    raise ValueError(
        "'index=False' is only valid when 'orient' is 'split' or 'table'"
    )

if lines and orient != "records":
    raise ValueError("'lines' keyword only valid when 'orient' is records")

if mode not in ["a", "w"]:
    msg = (
        f"mode={mode} is not a valid option."
        "Only 'w' and 'a' are currently supported."
    )
    raise ValueError(msg)

if mode == "a" and (not lines or orient != "records"):
    msg = (
        "mode='a' (append) is only supported when"
        "lines is True and orient is 'records'"
    )
    raise ValueError(msg)

if orient == "table" and isinstance(obj, Series):
    obj = obj.to_frame(name=obj.name or "values")

writer: type[Writer]
if orient == "table" and isinstance(obj, DataFrame):
    writer = JSONTableWriter
elif isinstance(obj, Series):
    writer = SeriesWriter
elif isinstance(obj, DataFrame):
    writer = FrameWriter
else:
    raise NotImplementedError("'obj' should be a Series or a DataFrame")

s = writer(
    obj,
    orient=orient,
    date_format=date_format,
    double_precision=double_precision,
    ensure_ascii=force_ascii,
    date_unit=date_unit,
    default_handler=default_handler,
    index=index,
    indent=indent,
).write()

if lines:
    s = convert_to_line_delimits(s)

if path_or_buf is not None:
    # apply compression and byte/text conversion
    with get_handle(
        path_or_buf, mode, compression=compression, storage_options=storage_options
    ) as handles:
        handles.handle.write(s)
else:
    exit(s)
exit(None)
