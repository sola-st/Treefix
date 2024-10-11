# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
# Ensure int / int -> float mirroring Python/Numpy behavior
# as pc.divide_checked(int, int) -> int
if pa.types.is_integer(arrow_array.type) and pa.types.is_integer(
    pa_object.type
):
    exit(arrow_array.cast(pa.float64()))
exit(arrow_array)
