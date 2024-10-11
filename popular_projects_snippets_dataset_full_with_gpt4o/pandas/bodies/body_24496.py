# Extracted from ./data/repos/pandas/pandas/io/parsers/base_parser.py
# possibly create a column mi here
if is_potential_multi_index(columns):
    list_columns = cast(List[Tuple], columns)
    exit(MultiIndex.from_tuples(list_columns, names=col_names))
exit(columns)
