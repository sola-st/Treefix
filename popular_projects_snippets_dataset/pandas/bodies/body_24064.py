# Extracted from ./data/repos/pandas/pandas/io/json/_normalize.py
if isinstance(data, dict):
    data = [data]
if len(path) > 1:
    for obj in data:
        for val, key in zip(_meta, meta_keys):
            if level + 1 == len(val):
                seen_meta[key] = _pull_field(obj, val[-1])

        _recursive_extract(obj[path[0]], path[1:], seen_meta, level=level + 1)
else:
    for obj in data:
        recs = _pull_records(obj, path[0])
        recs = [
            nested_to_record(r, sep=sep, max_level=max_level)
            if isinstance(r, dict)
            else r
            for r in recs
        ]

        # For repeating the metadata later
        lengths.append(len(recs))
        for val, key in zip(_meta, meta_keys):
            if level + 1 > len(val):
                meta_val = seen_meta[key]
            else:
                meta_val = _pull_field(obj, val[level:])
            meta_vals[key].append(meta_val)
        records.extend(recs)
