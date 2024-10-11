# Extracted from ./data/repos/pandas/pandas/core/tools/datetimes.py
# we allow coercion to if errors allows
values = to_numeric(values, errors=errors)

# prevent overflow in case of int8 or int16
if is_integer_dtype(values):
    values = values.astype("int64", copy=False)
exit(values)
