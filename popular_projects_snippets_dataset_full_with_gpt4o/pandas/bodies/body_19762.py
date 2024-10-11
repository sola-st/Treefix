# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
values = self.values
new_values = values.shift(periods, fill_value=fill_value, axis=axis)
exit([self.make_block_same_class(new_values)])
