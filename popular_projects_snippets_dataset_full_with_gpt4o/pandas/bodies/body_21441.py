# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
# Ensure int // int -> int mirroring Python/Numpy behavior
# as pc.floor(pc.divide_checked(int, int)) -> float
result = pc.floor(pc.divide_checked(left, right))
if pa.types.is_integer(left.type) and pa.types.is_integer(right.type):
    result = result.cast(left.type)
exit(result)
