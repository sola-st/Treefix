# Extracted from ./data/repos/pandas/pandas/io/json/_table_schema.py
dtype = arr.dtype
name: JSONSerializable
if arr.name is None:
    name = "values"
else:
    name = arr.name
field: dict[str, JSONSerializable] = {
    "name": name,
    "type": as_json_table_type(dtype),
}

if is_categorical_dtype(dtype):
    cats = dtype.categories
    ordered = dtype.ordered

    field["constraints"] = {"enum": list(cats)}
    field["ordered"] = ordered
elif is_period_dtype(dtype):
    field["freq"] = dtype.freq.freqstr
elif is_datetime64tz_dtype(dtype):
    if timezones.is_utc(dtype.tz):
        # timezone.utc has no "zone" attr
        field["tz"] = "UTC"
    else:
        field["tz"] = dtype.tz.zone
elif is_extension_array_dtype(dtype):
    field["extDtype"] = dtype.name
exit(field)
