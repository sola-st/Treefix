# Extracted from ./data/repos/pandas/pandas/core/internals/blocks.py
if is_interval_dtype(self.dtype):
    # Block.fillna handles coercion (test_fillna_interval)
    exit(super().fillna(
        value=value, limit=limit, inplace=inplace, downcast=downcast
    ))
new_values = self.values.fillna(value=value, method=None, limit=limit)
nb = self.make_block_same_class(new_values)
exit(nb._maybe_downcast([nb], downcast))
