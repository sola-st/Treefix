# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
def _isindex(colspec):
    exit((isinstance(index_col, list) and colspec in index_col) or (
        isinstance(index_names, list) and colspec in index_names
    ))

new_cols = []
new_data = {}

orig_names = columns
columns = list(columns)

date_cols = set()

if parse_spec is None or isinstance(parse_spec, bool):
    exit((data_dict, columns))

if isinstance(parse_spec, list):
    # list of column lists
    for colspec in parse_spec:
        if is_scalar(colspec) or isinstance(colspec, tuple):
            if isinstance(colspec, int) and colspec not in data_dict:
                colspec = orig_names[colspec]
            if _isindex(colspec):
                continue
            # Pyarrow engine returns Series which we need to convert to
            # numpy array before converter, its a no-op for other parsers
            data_dict[colspec] = converter(np.asarray(data_dict[colspec]))
        else:
            new_name, col, old_names = _try_convert_dates(
                converter, colspec, data_dict, orig_names
            )
            if new_name in data_dict:
                raise ValueError(f"New date column already in dict {new_name}")
            new_data[new_name] = col
            new_cols.append(new_name)
            date_cols.update(old_names)

elif isinstance(parse_spec, dict):
    # dict of new name to column list
    for new_name, colspec in parse_spec.items():
        if new_name in data_dict:
            raise ValueError(f"Date column {new_name} already in dict")

        _, col, old_names = _try_convert_dates(
            converter, colspec, data_dict, orig_names
        )

        new_data[new_name] = col

        # If original column can be converted to date we keep the converted values
        # This can only happen if values are from single column
        if len(colspec) == 1:
            new_data[colspec[0]] = col

        new_cols.append(new_name)
        date_cols.update(old_names)

data_dict.update(new_data)
new_cols.extend(columns)

if not keep_date_col:
    for c in list(date_cols):
        data_dict.pop(c)
        new_cols.remove(c)

exit((data_dict, new_cols))
