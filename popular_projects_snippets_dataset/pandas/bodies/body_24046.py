# Extracted from ./data/repos/pandas/pandas/io/json/_json.py

json = self.json
orient = self.orient

if orient == "columns":
    self.obj = DataFrame(
        loads(json, precise_float=self.precise_float), dtype=None
    )
elif orient == "split":
    decoded = {
        str(k): v
        for k, v in loads(json, precise_float=self.precise_float).items()
    }
    self.check_keys_split(decoded)
    orig_names = [
        (tuple(col) if isinstance(col, list) else col)
        for col in decoded["columns"]
    ]
    decoded["columns"] = dedup_names(
        orig_names,
        is_potential_multi_index(orig_names, None),
    )
    self.obj = DataFrame(dtype=None, **decoded)
elif orient == "index":
    self.obj = DataFrame.from_dict(
        loads(json, precise_float=self.precise_float),
        dtype=None,
        orient="index",
    )
elif orient == "table":
    self.obj = parse_table_schema(json, precise_float=self.precise_float)
else:
    self.obj = DataFrame(
        loads(json, precise_float=self.precise_float), dtype=None
    )
