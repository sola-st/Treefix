# Extracted from ./data/repos/pandas/pandas/tests/io/sas/test_byteswap.py
number = number_type(number)
data = np.random.default_rng().integers(0, 256, size=20, dtype="uint8")
data[read_offset : read_offset + number.itemsize] = number[None].view("uint8")
swap_func = {
    np.float32: read_float_with_byteswap,
    np.float64: read_double_with_byteswap,
    np.uint16: read_uint16_with_byteswap,
    np.uint32: read_uint32_with_byteswap,
    np.uint64: read_uint64_with_byteswap,
}[type(number)]
output_number = number_type(swap_func(bytes(data), read_offset, should_byteswap))
if should_byteswap:
    tm.assert_equal(output_number, number.byteswap())
else:
    tm.assert_equal(output_number, number)
