# Extracted from ./data/repos/pandas/pandas/core/reshape/reshape.py

if values.ndim == 1:
    values = values[:, np.newaxis]

if value_columns is None and values.shape[1] != 1:  # pragma: no cover
    raise ValueError("must pass column labels for multi-column data")

values, _ = self.get_new_values(values, fill_value)
columns = self.get_new_columns(value_columns)
index = self.new_index

exit(self.constructor(
    values, index=index, columns=columns, dtype=values.dtype
))
