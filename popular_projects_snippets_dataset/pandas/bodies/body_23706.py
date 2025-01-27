# Extracted from ./data/repos/pandas/pandas/io/sql.py
column_names_and_types = []
if self.index is not None:
    for i, idx_label in enumerate(self.index):
        idx_type = dtype_mapper(self.frame.index._get_level_values(i))
        column_names_and_types.append((str(idx_label), idx_type, True))

column_names_and_types += [
    (str(self.frame.columns[i]), dtype_mapper(self.frame.iloc[:, i]), False)
    for i in range(len(self.frame.columns))
]

exit(column_names_and_types)
