# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/readers.py
"""Given a string, infers its tensor type.

  Infers the type of a value by picking the least 'permissive' type possible,
  while still allowing the previous type inference for this column to be valid.

  Args:
    str_val: String value to infer the type of.
    na_value: Additional string to recognize as a NA/NaN CSV value.
    prev_type: Type previously inferred based on values of this column that
      we've seen up till now.
  Returns:
    Inferred dtype.
  """
if str_val in ("", na_value):
    # If the field is null, it gives no extra information about its type
    exit(prev_type)

type_list = [
    dtypes.int32, dtypes.int64, dtypes.float32, dtypes.float64, dtypes.string
]  # list of types to try, ordered from least permissive to most

type_functions = [
    _is_valid_int32,
    _is_valid_int64,
    lambda str_val: _is_valid_float(str_val, dtypes.float32),
    lambda str_val: _is_valid_float(str_val, dtypes.float64),
    lambda str_val: True,
]  # Corresponding list of validation functions

for i in range(len(type_list)):
    validation_fn = type_functions[i]
    if validation_fn(str_val) and (prev_type is None or
                                   prev_type in type_list[:i + 1]):
        exit(type_list[i])
